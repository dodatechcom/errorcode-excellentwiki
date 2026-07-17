---
title: "Vite Build Error — Rollup Failed"
description: "Vite production build fails during Rollup bundling."
tools: ["vite"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Vite Build Error — Rollup Failed

A Vite build error occurs when the Rollup-based production build fails during bundling, chunk splitting, or asset processing. The error identifies which module or plugin caused the failure.

## Common Causes

- A plugin is incompatible with the Rollup build pipeline
- A module contains syntax that cannot be bundled
- An import resolution fails during bundling
- The output configuration conflicts with the build target

## How to Fix

### Run Build with Debug Output

```bash
npx vite build --debug
```

### Check the Failing Module

```bash
npx vite build 2>&1 | grep -A 5 "error"
```

### Fix Plugin Compatibility

```javascript
// vite.config.js
import vue from '@vitejs/plugin-vue';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [vue()],
});
```

### Adjust Build Target

```javascript
export default defineConfig({
  build: {
    target: 'es2020',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },
});
```

### Increase Memory for Large Projects

```bash
NODE_OPTIONS='--max-old-space-size=4096' npx vite build
```

### Disable Code Splitting Temporarily

```javascript
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: () => 'everything',
      },
    },
  },
});
```

## Examples

```bash
npx vite build
[vite]: RollupError: Unexpected token in template
file: /src/App.vue:10:5

# Fix: update @vitejs/plugin-vue to match Vue version

# Out of memory
FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed
# Fix: NODE_OPTIONS='--max-old-space-size=4096' npx vite build
```

## Related Errors

- [Config Error]({{< relref "/tools/vite/config-error6" >}}) — invalid configuration
- [Plugin Error]({{< relref "/tools/vite/import-error8" >}}) — failed to resolve import
- [CSS Error]({{< relref "/tools/vite/css-error" >}}) — CSS processing failure
