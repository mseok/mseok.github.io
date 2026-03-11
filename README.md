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
