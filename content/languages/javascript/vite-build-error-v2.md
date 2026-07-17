---
title: "[Solution] Vite: Rollup Build Failed Fix"
description: "Fix Vite build failure when Rollup encounters errors during production bundling. Handle chunk size limits, missing modules, and asset issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite: Rollup Build Failed

This error occurs when `vite build` fails during the Rollup bundling phase. Unlike the standard build error (missing imports), this covers deeper Rollup failures such as chunk size limits, asset pipeline errors, and plugin conflicts.

## What This Error Means

Common error messages:

- `Build failed with errors.`
- `[vite]: RollupError: Total size of generated chunks "..." exceeds 500 kB`
- `[plugin:vite:esbuild] Transform failed`
- `error during build: Error: Unexpected "<"` (SSR misconfiguration)

Rollup processes all modules, tree-shakes unused code, splits chunks, and writes output. Any failure during these stages aborts the entire build.

## Common Causes

```javascript
// Cause 1: Chunk exceeds size warning threshold
// Large dependencies like lodash, moment, or monaco-editor inflate bundle

// Cause 2: Plugin version mismatch
// A Rollup plugin is incompatible with the current Vite version

// Cause 3: SSR build trying to bundle Node built-ins
import fs from 'fs'; // fails in client bundle

// Cause 4: Circular dependency detected during tree-shaking
// a.ts → b.ts → c.ts → a.ts

// Cause 5: Dynamic import with non-static argument
const mod = await import(`./lang/${locale}.js`);
```

## How to Fix

### Fix 1: Increase or suppress the chunk size limit

```javascript
// vite.config.js
export default defineConfig({
  build: {
    chunkSizeWarningLimit: 1000, // kB
  },
});
```

### Fix 2: Split large vendor chunks

```javascript
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          utils: ['lodash', 'date-fns'],
        },
      },
    },
  },
});
```

### Fix 3: Mark Node built-ins as external for SSR

```javascript
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      external: ['fs', 'path', 'url'],
    },
  },
});
```

### Fix 4: Fix circular dependencies

```bash
npx madge --circular src/
# Then refactor to break the cycle
```

### Fix 5: Use static imports for dynamic loading

```javascript
// Instead of this:
const mod = await import(`./lang/${locale}.js`);

// Use this:
const langMap = {
  en: () => import('./lang/en.js'),
  fr: () => import('./lang/fr.js'),
};
const mod = await langMap[locale]();
```

## Examples

```bash
$ vite build

vite v5.4.0 building for production...
✓ 423 modules transformed.
✗ Build failed with errors:
  "src/components/HeavyChart.tsx" is dynamically imported by
  "src/pages/Dashboard.tsx" but not statically imported by any static routes.
```

```javascript
// Fix: add a fallback or use a glob import
const modules = import.meta.glob('./components/*.tsx');
```

## Related Errors

- [Vite Build Error]({{< relref "/languages/javascript/vite-build-error" >}}) — rollup failed to resolve import
- [Vite HMR Error]({{< relref "/languages/javascript/vite-hmr-error" >}}) — HMR update failed
- [esbuild Error]({{< relref "/languages/javascript/esbuild-error" >}}) — esbuild transform failed
