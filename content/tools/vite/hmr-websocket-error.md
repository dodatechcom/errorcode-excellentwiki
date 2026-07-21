---
title: "[Solution] Vite HMR WebSocket Error"
description: "Fix Vite HMR WebSocket errors. Resolve issues when hot module replacement WebSocket connection fails."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite HMR WebSocket Error

Fix Vite HMR WebSocket errors. Resolve issues when hot module replacement WebSocket connection fails.

## Common Causes

- WebSocket URL is blocked by a browser extension or firewall
- Dev server host configuration does not match the client access URL
- SSL certificate mismatch between the server and the WebSocket URL
- Multiple Vite instances on different ports cause WebSocket conflicts

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