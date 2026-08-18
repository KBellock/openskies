# Open Skies PhotoForecast — website

Static marketing, support, and privacy site for the **Open Skies PhotoForecast**
iOS app. No build step: plain HTML + one stylesheet, served by GitHub Pages.

## Pages

| File | Purpose | App Store Connect field |
| --- | --- | --- |
| `index.html` | Marketing landing page | Marketing URL (optional) |
| `support.html` | Contact + FAQ | **Support URL** (required) |
| `privacy.html` | Privacy policy | **Privacy Policy URL** (required) |

`privacy.html` is a verbatim rendering of `PRIVACY.md` in the app repo. When that
file changes, update this page to match and bump the "Last updated" date in both.

## Local preview

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploying

Pushed to `main`; GitHub Pages serves the repo root. `.nojekyll` is present so
Pages copies files as-is rather than running Jekyll.

## Assets

- `assets/emblem.svg` — aperture-iris mark, drawn as SVG (favicon + brand + hero).
- `assets/app-icon.png`, `assets/favicon.png` — copied from the app's `assets/`.

Brand: background `#0a0d12`, surface `#111620`, amber `#f0a500`, text `#e6edf3`.
