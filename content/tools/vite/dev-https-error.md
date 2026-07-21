---
title: "[Solution] Vite Dev HTTPS Error"
description: "Fix Vite dev server HTTPS errors. Resolve issues when the development server cannot start with HTTPS."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite Dev HTTPS Error

Fix Vite dev server HTTPS errors. Resolve issues when the development server cannot start with HTTPS.

## Common Causes

- Certificate file path in the server.https config does not exist
- Private key does not match the certificate provided for HTTPS
- mkcert is not installed for generating local trusted certificates
- Certificate has expired and needs to be regenerated

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