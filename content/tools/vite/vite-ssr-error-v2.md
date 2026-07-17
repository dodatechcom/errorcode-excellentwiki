---
title: "Vite SSR Server-Side Render Error"
description: "Vite SSR build or server-side rendering fails."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "ssr", "server-side", "render", "node"]
weight: 5
---

# Vite SSR — Server-Side Render Error

This error occurs when Vite's server-side rendering (SSR) fails during build or runtime. The SSR module cannot be loaded or executed on the server.

## Common Causes

- Browser-only code used in SSR context
- Missing SSR-compatible dependencies
- `import.meta` used in server code
- CSS imports not handled in SSR

## How to Fix

### Configure SSR Build

```javascript
// vite.config.js
export default defineConfig({
  build: {
    ssr: true,
  },
  ssr: {
    noExternal: ['some-esm-package'],
  },
});
```

### Mark Non-SSR Dependencies

```javascript
export default defineConfig({
  ssr: {
    noExternal: ['package-that-needs-bundling'],
    external: ['package-only-for-browser'],
  },
});
```

### Fix Browser-Only Code

```javascript
// Check for browser-only APIs
if (typeof window !== 'undefined') {
  // Browser-only code
  document.getElementById('app');
}
```

### Handle CSS Imports in SSR

```javascript
// vite.config.js
export default defineConfig({
  ssr: {
    format: 'cjs',
  },
  css: {
    modules: {
      localsConvention: 'camelCase',
    },
  },
});
```

### Run SSR Dev Server

```bash
npx vite --ssr
```

### Fix Node.js Module Resolution

```javascript
// Use conditional imports
const isNode = typeof process !== 'undefined' && process.versions?.node;

if (isNode) {
  const fs = await import('fs');
}
```

## Examples

```text
[vite] Internal server error: SSR module "src/App.vue"
  failed to load. Is it a browser-only module?
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Dev Server Error]({{< relref "/tools/vite/vite-dev-server-error" >}}) — dev server issues
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
