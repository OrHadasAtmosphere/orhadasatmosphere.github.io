# Or Hadas — atmospheric scientist

Academic website for Or Hadas, Hess Postdoctoral Fellow at Princeton University working with Stephan Fueglistaler.

## Maintain the site

A static GitHub Pages site with no third-party build dependencies. `.nojekyll` tells GitHub Pages to serve the committed HTML directly.

- Edit biography, research text, and shared layout in `scripts/build.py`.
- Edit papers in `_data/publications.json`. Set `status` to `preprint`, `published`, or `report`.
- Edit visual styles in `assets/css/custom.css`.
- Replace the portrait at `assets/img/20176F053.jpg` or the CV at `assets/files/CV_Or_Hadas.pdf` as needed. The existing CV is preserved unchanged.

Build and validate using Python 3.9 or later:

```bash
python scripts/build.py
python scripts/check.py
python -m http.server 8000
```

Open http://localhost:8000 to preview. Commit generated HTML together with source changes.

## Publish

GitHub Pages should deploy from the main branch and root directory. Push changes to a branch and merge into main to publish.

The local checkout uses a repository-specific SSH deploy key with write access. Its private key is stored outside this checkout and must never be committed. The checkout's local Git configuration selects the key. The chat app's GitHub connection is independent.

## Publication verification (November 2026)

Current role and supervisor were supplied by Or Hadas. Existing journal publications were retained. New preprints, author names, and repaired publication links were checked against primary records:

- https://arxiv.org/abs/2609.16671
- https://arxiv.org/abs/2608.12666
- https://arxiv.org/abs/2607.02213 (updated v2 title)
- https://doi.org/10.1029/2025GL118496
- https://doi.org/10.1029/2025GL118886
- https://doi.org/10.1038/s41467-026-71784-3

Google Scholar: https://scholar.google.com/citations?user=gYHd_jcAAAAJ&sortby=pubdate . Direct profile access was unavailable during the update, so the list was checked against the primary records above.

Additional publication sources:

- https://doi.org/10.22541/essoar.15005264/v1
- https://mpimet.mpg.de/en/staff/franziska-glassmeier
- https://doi.org/10.17617/2.3711842

The equal-contribution designation for the dynamical-regimes preprint was supplied by Or Hadas.

## Contact address

The contact address is decoded in the browser only when a visitor clicks “Reveal email.” Plain-text addresses and static mailto links are omitted from generated pages; visitors without JavaScript see an `[at]` / `[dot]` fallback. This deters basic scrapers, but sophisticated crawlers can still recover the address. Update the encoded character list in `assets/js/contact.js` and the noscript fallback in `scripts/build.py` together.
