---
title: "[Solution] Laravel Asset Versioning Mix/Vite Error"
description: "Fix Laravel mix manifest not found or Vite manifest error. Resolve asset versioning and cache busting issues."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the application tries to resolve a versioned asset URL but the manifest file (Mix or Vite) is missing or corrupt.

## Common Causes

- Assets were not compiled before deployment
- `public/mix-manifest.json` or `public/build/manifest.json` is missing
- Vite dev server is not running in development mode
- `npm run build` was not executed during CI/CD
- Manifest file is gitignored and not deployed

## How to Fix

1. Compile assets before deployment:

```bash
npm install && npm run build
# or for Vite
npm run build
```

2. Verify the manifest file exists:

```bash
ls -la public/build/manifest.json  # Vite
ls -la public/mix-manifest.json     # Mix
```

3. For Vite in development, start the dev server:

```bash
npm run dev
# or
php artisan vite:dev
```

4. Use the correct helper in Blade:

```html
<!-- Vite -->
@vite(['resources/css/app.css', 'resources/js/app.js'])

<!-- Mix -->
<link rel="stylesheet" href="{{ mix('css/app.css') }}">
```

## Examples

```html
<!-- Blade template fails when manifest is missing -->
@vite(['resources/js/app.js'])
// ViteManifestNotFoundException: Vite manifest not found at:
// /var/www/html/public/build/manifest.json

<!-- Mix fails when manifest is missing -->
<script src="{{ mix('js/app.js') }}"></script>
// InvalidArgumentException: Mix manifest not found.
```
