---
title: "Pre-transform Error"
description: "Vite failed during the pre-transformation phase, unable to process a module before serving or bundling."
tools: ["vite"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error occurs when Vite's pre-bundling step (powered by esbuild) fails to transform a dependency. It usually happens before the dev server can serve the module.

## Common Causes

- The dependency contains syntax that esbuild cannot parse
- A CommonJS module has compatibility issues with Vite's ESM-based pipeline
- The `optimizeDeps.include` configuration is missing a problematic package
- A file contains invalid JavaScript or TypeScript syntax

## How to Fix

Force Vite to re-optimize dependencies:

```bash
rm -rf node_modules/.vite
npm run dev
```

Exclude the problematic dependency from optimization:

```javascript
// vite.config.js
export default defineConfig({
  optimizeDeps: {
    exclude: ['problematic-package'],
  },
});
```

Or explicitly include it for pre-bundling:

```javascript
// vite.config.js
export default defineConfig({
  optimizeDeps: {
    include: ['some-package'],
  },
});
```

## Examples

```
Pre-transform error: "src/utils/helper.ts"
SyntaxError: Unexpected token (note: dependencies are pre-bundled with esbuild)

  at src/utils/helper.ts:12:5
```

## Related Errors

- [SSR Error]({{< relref "/tools/vite/ssr-error" >}})
