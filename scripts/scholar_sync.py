"""Refresh _data/scholar.json from a public Google Scholar profile.

Standard library only and no model calls. The file is rewritten only when the
publication list changes; `updated` records the date of that change (KST).
Display overrides live in _data/publications.yml and are applied by the templates.
"""

import argparse
import datetime
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

PROFILE_URL = "https://scholar.google.com/citations?user={user}&hl=en&cstart={start}&pagesize={size}&sortby=pubdate"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)
PAGE_SIZE = 100
ROW = re.compile(r'<tr class="gsc_a_tr">(.*?)</tr>', re.S)
KST = datetime.timezone(datetime.timedelta(hours=9))


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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", required=True, help="Scholar profile id, e.g. U1j8Ip8AAAAJ")
    parser.add_argument("--out", type=Path, default=Path("_data/scholar.json"))
    args = parser.parse_args()

    publications = fetch(args.user)
    previous = json.loads(args.out.read_text(encoding="utf-8")) if args.out.exists() else {}
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
