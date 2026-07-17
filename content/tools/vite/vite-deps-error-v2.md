---
title: "Vite Pre-Bundling OptimizeDeps Error"
description: "Vite pre-bundling (optimizeDeps) fails for dependencies."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "optimize", "deps", "pre-bundle", "dependency"]
weight: 5
---

# Vite Pre-Bundling — optimizeDeps Error

This error occurs when Vite's pre-bundling (optimizeDeps) step fails. Vite pre-bundles dependencies to improve dev server performance, but some packages may fail during this process.

## Common Causes

- Dependency uses CommonJS in a way Vite cannot handle
- Dependency has ESM/CJS dual package issues
- Dependency requires native compilation
- Pre-bundled cache is corrupted

## How to Fix

### Clear Pre-Bundled Cache

```bash
rm -rf node_modules/.vite
npx vite
```

### Force Pre-Bundling

```bash
npx vite --force
```

### Include Problematic Dependency

```javascript
// vite.config.js
export default defineConfig({
  optimizeDeps: {
    include: ['problematic-package'],
  },
});
```

### Exclude Problematic Dependency

```javascript
export default defineConfig({
  optimizeDeps: {
    exclude: ['package-that-fails-to-bundle'],
  },
});
```

### Configure Pre-Bundling Options

```javascript
export default defineConfig({
  optimizeDeps: {
    esbuildOptions: {
      target: 'es2020',
    },
    force: true,
  },
});
```

### Fix Native Module Issues

```bash
npm rebuild
npx vite --force
```

## Examples

```text
[vite] Pre-transform error for /node_modules/.vite/deps/chunk.js:
  ERROR: Cannot bundle "native-module" as it uses Node.js APIs

[vite] Pre-bundling failed for "problematic-package"
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
