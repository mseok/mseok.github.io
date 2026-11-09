"""Refresh _data/scholar.json from a public Google Scholar profile.

Standard library only and no model calls. The file is rewritten only when the
publication list changes; `updated` records the date of that change (KST).
Scholar's list page gives only the year, and its per-paper pages answer scripts
with a bot check, so an entry without a date gets one by exact title match from
Crossref (journals, bioRxiv and other posted content) and arXiv (first version):
the earliest public date of that title.
Display overrides live in _data/publications.yml and are applied by the templates.
"""

import argparse
import datetime
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

PROFILE_URL = "https://scholar.google.com/citations?user={user}&hl=en&cstart={start}&pagesize={size}&sortby=pubdate"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)
PAGE_SIZE = 100
ROW = re.compile(r'<tr class="gsc_a_tr">(.*?)</tr>', re.S)
KST = datetime.timezone(datetime.timedelta(hours=9))
LOOKUP_AGENT = "mseok.github.io-scholar-sync/1.0"
CROSSREF = "https://api.crossref.org/works?rows=10&query.title={query}"
ARXIV = "https://export.arxiv.org/api/query?max_results=5&search_query=ti:%22{query}%22"
ATOM = "{http://www.w3.org/2005/Atom}"


def text(fragment: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).replace("\xa0", " ").strip()


def venue(source: str) -> str:
    """Shorten Scholar's source line: drop the trailing year, preprint numbers and volume/issue/pages."""
    s = re.sub(r",\s*(\d{4}|0)$", "", source).strip()
    for server in ("bioRxiv", "ChemRxiv", "medRxiv", "arXiv"):
        if s.lower().startswith(server.lower()):
            return server
    return re.sub(r"\s+\d+\s*(\(\d+\))?(,\s*[\w.-]+)?$", "", s)


def parse(page: str) -> list[dict]:
    publications = []
    for row in ROW.findall(page):
        link = re.search(r'href="([^"]+)" class="gsc_a_at">(.*?)</a>', row, re.S)
        grays = re.findall(r'<div class="gs_gray">(.*?)</div>', row, re.S)
        year = re.search(r'<span class="gsc_a_h gsc_a_hc gs_ibl">(\d{4})</span>', row)
        article = re.search(r"citation_for_view=[^:&]+:([^&]+)", html.unescape(link.group(1))).group(1)
        publications.append({
            "id": article,
            "title": text(link.group(2)),
            "authors": text(grays[0]),
            "venue": venue(text(grays[1])) if len(grays) > 1 else "",
            "year": int(year.group(1)) if year else None,
        })
    return publications


def fetch(user: str) -> list[dict]:
    publications: list[dict] = []
    while True:
        url = PROFILE_URL.format(user=user, start=len(publications), size=PAGE_SIZE)
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "en"})
        with urllib.request.urlopen(request, timeout=30) as response:
            page = response.read().decode("utf-8")
        rows = parse(page)
        if not rows and not publications:
            sys.exit("Scholar returned no publication rows (likely a bot check); data left unchanged.")
        publications += rows
        if len(rows) < PAGE_SIZE:
            return publications
        time.sleep(5)


def same_title(a: str, b: str) -> bool:
    def norm(s: str) -> str:
        return re.sub(r"[^a-z0-9]", "", html.unescape(s).lower())
    return norm(a) == norm(b)


def get(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": LOOKUP_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def crossref_date(title: str) -> str | None:
    """Earliest full date among Crossref records whose title matches exactly."""
    items = json.loads(get(CROSSREF.format(query=urllib.parse.quote(title))))["message"]["items"]
    dates = []
    for item in items:
        if not any(same_title(title, t) for t in item.get("title", [])):
            continue
        parts = (item.get("posted") or item.get("published") or {}).get("date-parts", [[]])[0]
        if len(parts) == 3:
            dates.append("{:04d}-{:02d}-{:02d}".format(*parts))
        elif parts and item.get("created", {}).get("date-time", "")[:4] <= str(parts[0]):
            # A year-only record: the DOI registration date stands in unless it
            # came after that year (DOIs deposited in bulk long after publication).
            dates.append(item["created"]["date-time"][:10])
    return min(dates) if dates else None


def arxiv_date(title: str) -> str | None:
    """Date of the first arXiv version whose title matches exactly."""
    query = urllib.parse.quote(re.sub(r"[^\w\s-]", " ", title))
    feed = ET.fromstring(get(ARXIV.format(query=query)))
    dates = [
        entry.findtext(f"{ATOM}published", "")[:10]
        for entry in feed.iter(f"{ATOM}entry")
        if same_title(title, " ".join(entry.findtext(f"{ATOM}title", "").split()))
    ]
    return min(dates) if dates else None


def add_dates(publications: list[dict], previous: dict) -> None:
    """Keep dates found earlier; look up the rest in Crossref and arXiv (earliest wins)."""
    for pub in publications:
        known = previous.get(pub["id"], {}).get("date")
        if known:
            pub["date"] = known
            continue
        found = []
        for lookup in (crossref_date, arxiv_date):
            try:
                date = lookup(pub["title"])
            except (urllib.error.URLError, TimeoutError, ET.ParseError, KeyError, ValueError) as error:
                print(f"{lookup.__name__} failed for {pub['title']!r}: {error}")
                continue
            finally:
                time.sleep(3)
            if date:
                found.append(date)
        if found:
            pub["date"] = min(found)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", required=True, help="Scholar profile id, e.g. U1j8Ip8AAAAJ")
    parser.add_argument("--out", type=Path, default=Path("_data/scholar.json"))
    args = parser.parse_args()

    publications = fetch(args.user)
    previous = json.loads(args.out.read_text(encoding="utf-8")) if args.out.exists() else {}
    add_dates(publications, {p["id"]: p for p in previous.get("publications", [])})
    if previous.get("publications") == publications:
        print(f"No change ({len(publications)} entries).")
        return
    data = {
        "profile": args.user,
        "updated": datetime.datetime.now(KST).date().isoformat(),
        "publications": publications,
    }
    args.out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    old = {p["id"] for p in previous.get("publications", [])}
    added = [p["title"] for p in publications if p["id"] not in old]
    print(f"Updated {args.out}: {len(publications)} entries; new: {added or 'none'}")


if __name__ == "__main__":
    main()
