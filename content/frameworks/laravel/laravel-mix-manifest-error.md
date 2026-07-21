---
title: "[Solution] Laravel Mix Manifest Not Found Error"
description: "Fix Laravel Mix manifest not found exception. Resolve missing mix-manifest.json after asset compilation in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Laravel tries to resolve a versioned asset URL via `mix()` but the `mix-manifest.json` file does not exist in the public directory.

## Common Causes

- `npm run dev` or `npm run prod` was never run after setup
- `public/mix-manifest.json` is listed in `.gitignore` and not deployed
- Asset compilation failed silently during CI/CD
- Webpack or Vite output directory does not match expected location
- `node_modules` was not installed on the build server

## How to Fix

1. Compile assets and verify manifest exists:

```bash
npm install
npm run dev    # development with hot reload
npm run prod   # production with minification
```

2. Check `.gitignore` does not exclude the manifest:

```text
# .gitignore -- do NOT add these lines
# public/mix-manifest.json
# public/build/
```

3. Use the correct mix helper in Blade:

```html
<link rel="stylesheet" href="{{ mix('css/app.css') }}">
<script src="{{ mix('js/app.js') }}"></script>
```

4. For Docker builds, copy compiled assets into the image:

```dockerfile
COPY --from=build /app/public/mix-manifest.json /app/public/
COPY --from=build /app/public/css /app/public/css
COPY --from=build /app/public/js /app/public/js
```

## Examples

```php
// Blade template fails when manifest is missing
<link href="{{ mix('css/app.css') }}" rel="stylesheet">
// InvalidArgumentException: Mix manifest not found at:
// /var/www/html/public/mix-manifest.json

// Verify the file exists
file_exists(public_path('mix-manifest.json')); // false if missing
```
