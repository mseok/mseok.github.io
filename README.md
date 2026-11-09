# mseok.github.io

Jekyll source for `https://mseok.github.io/`, using the Moonwalk theme with a safe staging flow.

## Requirements

- `mise`
- `git`
- Homebrew packages: `libyaml`, `openssl@3`, `readline`, `gmp`

This repository does not rely on a globally installed `jekyll`. All commands should run through the repo scripts.

## Local Setup

```bash
mise install
bin/setup
```

`bin/setup` will install the required Homebrew packages if they are missing.

## Local Development

```bash
bin/serve
```

The development server defaults to `http://127.0.0.1:4000`.

## Local Build

```bash
bin/build
```

## Preview Build

```bash
bin/build-preview
```

This builds the site into `_site_preview/` with `baseurl: /mseok-preview` for the staging Pages repo.

## Preview Deployment

Preview deploys from the `codex/moonwalk-jekyll-migration` branch to `https://mseok.github.io/mseok-preview/` through `.github/workflows/deploy-preview.yml`.

The workflow expects a repository secret named `PREVIEW_REPO_TOKEN` in `mseok.github.io`.

- Create a fine-grained PAT with `Contents: Read and write` on `mseok-preview`.
- Add it as the `PREVIEW_REPO_TOKEN` secret in this repository.
- Push `codex/moonwalk-jekyll-migration` to trigger the workflow.

## Production

Production remains on the `main` branch until the staging site is approved. After approval, merge the migration branch into `main` and keep GitHub Pages serving from `main` `/`.

## Publications and Google Scholar

The home page renders publications from two data files:

- `_data/scholar.json` is generated from the public Google Scholar profile by `scripts/scholar_sync.py` (Python standard library, no model calls). It is rewritten only when the list changes. Scholar's list page gives only years, so the script adds each entry's first public date (preprints included) by exact title match in Crossref and arXiv; the lists are sorted by year, then that date.
- `_data/publications.yml` holds display overrides keyed by the Scholar article id: full author names, venue, year, links, `hidden`, and the `selected`, `short`, `summary` and `contribution` fields for the Selected section. Values here win over Scholar's.

The weekly run happens on the owner's own computer through a scheduled job (Mondays 06:23 KST): it pulls `main`, runs the script and commits and pushes `_data/scholar.json` only when it changed. Google Scholar answers GitHub-hosted runners with HTTP 403, so `.github/workflows/scholar-sync.yml` is kept for manual dispatch only. A new Scholar entry appears on the page automatically with Scholar's own fields; add an override when its authors or venue need cleaning up. If Scholar answers with a bot check, the script exits with an error and leaves the data unchanged.

Run it locally with:

```bash
python3 scripts/scholar_sync.py --user U1j8Ip8AAAAJ
```

## CV

`cv.pdf` is the CV from the private `mseok/AcademicCV` repository (synced with Overleaf). Its publication list, `publications.tex`, is generated from the same two data files by `scripts/cv_publications.rb` (Ruby standard library, no model calls), using the `cv.venues` and `cv.note` fields of `_data/publications.yml`; edit those fields here rather than `publications.tex`. The weekly job regenerates `publications.tex`, pushes it to AcademicCV when it changed, rebuilds the PDF with `latexmk -norc` and no shell escape whenever the AcademicCV source changed, and commits `cv.pdf` here. Edits made in Overleaf reach the PDF after Overleaf pushes them to GitHub; changes the job pushes to AcademicCV appear in Overleaf after "Pull GitHub changes into Overleaf".

```bash
ruby scripts/cv_publications.rb . ../AcademicCV/publications.tex
```
