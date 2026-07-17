---
title: "Vite Build Rollup Plugin Error"
description: "Vite production build fails with a Rollup plugin error."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "build", "rollup", "plugin", "production"]
weight: 5
---

# Vite Build — Rollup Plugin Error

This error occurs when a Rollup plugin fails during the Vite production build. The plugin encounters an issue it cannot handle, preventing the build from completing.

## Common Causes

- Plugin incompatible with Rollup API
- Plugin configuration is incorrect
- Plugin throws an unhandled exception
- Version mismatch between Vite and plugin

## How to Fix

### Run Build with Debug Output

```bash
npx vite build --debug
```

### Check Plugin Compatibility

```bash
npm ls vite @vitejs/plugin-react
```

### Update Plugins

```bash
npm install @vitejs/plugin-react@latest
```

### Fix Plugin Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
});
```

### Disable Problematic Plugin Temporarily

```javascript
export default defineConfig({
  plugins: [
    // problematicPlugin(),  // disable temporarily
  ],
});
```

### Increase Memory for Plugin

```bash
NODE_OPTIONS='--max-old-space-size=4096' npx vite build
```

## Examples

```text
vite v5.0.0 building for production...
[plugin:vite:esbuild] Transform failed with 1 error:
Unexpected token in template

RollupError: plugin failed to transform
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin transform error
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
