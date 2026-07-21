---
title: "[Solution] Vite SSR External Error"
description: "Fix Vite SSR external errors. Resolve issues when SSR externalization configuration is incorrect."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite SSR External Error

Fix Vite SSR external errors. Resolve issues when SSR externalization configuration is incorrect.

## Common Causes

- Package is externalized but has no CommonJS build for SSR
- ssr.external includes a package that should be bundled instead
- Package is both externalized and listed in ssr.noExternal causing conflict
- SSR externalized package uses require but the runtime is ESM only

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