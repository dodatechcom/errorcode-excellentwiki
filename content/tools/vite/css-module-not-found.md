---
title: "[Solution] Vite CSS Module Not Found"
description: "Fix Vite CSS module not found errors. Resolve issues when CSS modules fail to load or resolve."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite CSS Module Not Found

Fix Vite CSS module not found errors. Resolve issues when CSS modules fail to load or resolve.

## Common Causes

- CSS module file is imported with incorrect file extension in the path
- CSS modules feature is disabled in the vite configuration file
- Class name in the template does not match the exported CSS module property
- PostCSS is configured but conflicts with the CSS modules plugin

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