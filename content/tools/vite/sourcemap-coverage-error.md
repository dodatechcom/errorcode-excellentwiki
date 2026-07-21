---
title: "[Solution] Vite Sourcemap Coverage Error"
description: "Fix Vite source map coverage errors. Resolve issues when code coverage source maps are incorrect."
tools: ["vite"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vite Sourcemap Coverage Error

Fix Vite source map coverage errors. Resolve issues when code coverage source maps are incorrect.

## Common Causes

- Coverage tool generates a map that does not match the transformed code
- Source map uses an older version that the coverage tool cannot read
- Instrumentation plugin adds code that shifts source map line numbers
- Inline source map is embedded but the coverage tool expects a file

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