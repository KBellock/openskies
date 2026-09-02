# Open Skies PhotoForecast — website

Static marketing, support, and privacy site for the **Open Skies PhotoForecast**
iOS app. No build step: plain HTML + one stylesheet, served by GitHub Pages at
<https://openskiesapp.com>.

## Pages

| File | Purpose | App Store Connect field |
| --- | --- | --- |
| `index.html` | Marketing landing page | Marketing URL (optional) |
| `support.html` | Contact + FAQ | **Support URL** (required) |
| `privacy.html` | Privacy policy | **Privacy Policy URL** (required) |

`privacy.html` is the **source of truth** for the privacy policy text. The app
repo links to it (`PRIVACY_URL` in `lib/premium/config.ts`) and its `PRIVACY.md`
is only a pointer here, so edit the policy in this file and bump the
"Last updated" date when you do. Nothing needs syncing on the app side.

## Local preview

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploying

Pushed to `main`; GitHub Pages serves the repo root. `.nojekyll` is present so
Pages copies files as-is rather than running Jekyll. `CNAME` binds the custom
domain `openskiesapp.com` (DNS is on Cloudflare: four apex `A` records to
GitHub's Pages IPs, plus `www` as a `CNAME` — all unproxied / DNS-only).

## Assets

- `assets/emblem.svg` — aperture-iris mark, drawn as SVG (favicon + brand + hero).
- `assets/app-icon.png`, `assets/favicon.png` — copied from the app's `assets/`.

Brand: background `#0a0d12`, surface `#111620`, amber `#f0a500`, text `#e6edf3`.
