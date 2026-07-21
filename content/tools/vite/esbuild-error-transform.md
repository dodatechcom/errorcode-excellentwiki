---
title: "[Solution] Vite ESBuild Transform Error"
description: "Fix Vite esbuild transform errors. Resolve issues when esbuild fails to transform source code."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite ESBuild Transform Error

Fix Vite esbuild transform errors. Resolve issues when esbuild fails to transform source code.

## Common Causes

- Source file contains syntax that the esbuild target version does not support
- JSX factory function is not configured for the project JSX syntax
- TypeScript enum syntax is used but esbuild is configured to skip enums
- Decorator syntax is not supported by the current esbuild target

## How to Fix

### Check vite.config.js

Verify your Vite configuration includes the correct settings.

```javascript
// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  // Ensure correct configuration
  build: {
    target: 'esnext',
  },
});
```

### Clear the Vite Cache

Delete the node_modules/.vite directory to reset the pre-bundle cache.

```bash
rm -rf node_modules/.vite
npx vite
```

### Update Dependencies

Ensure all Vite-related packages are on compatible versions.

```bash
npm update vite @vitejs/plugin-react
```

### Enable Debug Logging

Run Vite with the --debug flag to see detailed internal logs.

## Examples

```javascript
// vite.config.js - Example fix
import { defineConfig } from 'vite';

export default defineConfig({
  optimizeDeps: {
    include: ['dep'],
  },
});
```