---
title: "Vite Tailwind PostCSS Plugin Error"
description: "Vite fails to process Tailwind CSS due to PostCSS plugin error."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite Tailwind — PostCSS Plugin Error

This error occurs when Vite fails to process Tailwind CSS due to a PostCSS plugin error. The Tailwind plugin may not be configured correctly or has a version incompatibility.

## Common Causes

- Tailwind CSS plugin not in PostCSS config
- PostCSS plugin version mismatch
- Invalid Tailwind configuration
- Missing PostCSS dependencies

## How to Fix

### Install Required Packages

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Create PostCSS Config

```javascript
// postcss.config.js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

### Configure Tailwind in Vite

```javascript
// vite.config.js
export default defineConfig({
  css: {
    postcss: './postcss.config.js',
  },
});
```

### Fix Tailwind Config

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

### Fix Tailwind v4 Migration

```bash
npm install tailwindcss @tailwindcss/vite
```

```javascript
// vite.config.js
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [tailwindcss()],
});
```

## Examples

```text
[vite] Internal server error:
  postcss-import: Failed to resolve "@tailwind base"
  at src/styles/main.css:1:1
```

## Related Errors

- [Vite CSS Error]({{< relref "/tools/vite/vite-css-error" >}}) — CSS processing failure
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
