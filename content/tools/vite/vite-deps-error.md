---
title: "Vite Pre-bundling Error — Dependencies"
description: "Vite fails to pre-bundle dependencies during dev server startup."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite Pre-bundling Error — Dependencies

A Vite pre-bundling error occurs when Vite's dependency optimization (using esbuild) fails during dev server startup. Vite pre-bundles node_modules dependencies to speed up page loading.

## Common Causes

- A dependency has invalid ESM/CJS syntax
- Dependency resolution conflicts
- esbuild fails to bundle certain packages
- Corrupted pre-bundle cache

## How to Fix

### Clear Pre-bundle Cache

```bash
rm -rf node_modules/.vite
```

### Restart Dev Server

```bash
npx vite --force
```

### Force Re-optimization

```javascript
// vite.config.js
export default defineConfig({
  optimizeDeps: {
    force: true,
    // Exclude problematic packages
    exclude: ['problematic-package'],
  },
});
```

### Include Problematic Packages

```javascript
export default defineConfig({
  optimizeDeps: {
    include: ['broken-esm-package'],
  },
});
```

### Check for CJS/ESM Conflicts

```bash
node -e "const pkg = require('./node_modules/package/package.json'); console.log(pkg.type)"
```

### Add Dependency to optimizeDeps

```javascript
export default defineConfig({
  optimizeDeps: {
    include: ['vue', 'vue-router'],
  },
});
```

## Examples

```bash
npx vite
[vite] Pre-bundling failed: Error: failed to resolve import 'vue' from 'node_modules/.vite/deps/vue.js'

# Fix:
rm -rf node_modules/.vite
npx vite --force
```

## Related Errors

- [Dev Server Error]({{< relref "/tools/vite/dev-server-error" >}}) — dev server issues
- [Import Error]({{< relref "/tools/vite/import-error8" >}}) — import resolution failure
- [Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — build failure
