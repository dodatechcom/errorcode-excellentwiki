---
title: "[Solution] Vite Dev Server CORS Error"
description: "Fix Vite dev server CORS errors. Resolve issues when cross-origin requests are blocked."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite Dev Server CORS Error

Fix Vite dev server CORS errors. Resolve issues when cross-origin requests are blocked.

## Common Causes

- CORS origin configuration is set to a restrictive value
- Browser sends a preflight request that the dev server does not handle
- Credentials are included but the Access-Control-Allow-Credentials header is missing
- Origin header value does not match the configured allowed origins

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