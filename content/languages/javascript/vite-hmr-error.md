---
title: "[Solution] Vite HMR Error: failed to update module Fix"
description: "Fix Vite HMR (Hot Module Replacement) errors when module updates fail. Resolve invalidation, circular dependencies, and HMR boundary issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite HMR Error — failed to update module

This error occurs when Vite's Hot Module Replacement fails to apply a module update to the running application. The browser console shows the HMR update failed.

## What This Error Means

Common error messages:

- `[vite] hmr error: failed to update module`
- `[vite] failed to apply HMR: ...`
- `[vite] module dependency no longer available`

HMR requires each module to have a valid HMR boundary — a module that accepts updates. When the chain is broken, updates fail.

## Common Causes

```javascript
// Cause 1: Module has side effects that can't be re-executed
import './polyfill'; // runs once, can't be re-applied

// Cause 2: Circular module dependency
// a.js → b.js → a.js

// Cause 3: Dynamic import without HMR boundary
const module = await import('./dynamic.js');

// Cause 4: Module exports changed structure
// Removed or renamed exports between saves

// Cause 5: Using CommonJS in ESM project
const { something } = require('./module');
```

## How to Fix

### Fix 1: Add HMR boundary

```javascript
// src/main.js
import { createApp } from 'vue';
import App from './App.vue';

const app = createApp(App);
app.mount('#app');

if (import.meta.hot) {
  import.meta.hot.accept();
}
```

### Fix 2: Handle CSS HMR

```javascript
// Add CSS HMR support
if (import.meta.hot) {
  import.meta.hot.accept('./styles.css', (newStyles) => {
    document.head.replaceChild(newStyles, styleElement);
  });
}
```

### Fix 3: Use import.meta.hot in component files

```javascript
// src/components/App.js
export function render() {
  return '<div>Hello</div>';
}

if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    if (newModule) {
      newModule.render(); // re-render with new exports
    }
  });
}
```

### Fix 4: Clear Vite cache

```bash
# Remove node_modules/.vite
rm -rf node_modules/.vite

# Restart dev server
npm run dev
```

### Fix 5: Use --force flag

```bash
# Force full reload
npx vite --force

# Or clear cache and restart
npx vite --clearScreen
```

## Examples

```javascript
// This can cause HMR failure
// bad.js
export const config = { debug: true };

// If you remove 'debug' while running, HMR may fail
// because other modules importing 'debug' break

// Fix: use named exports carefully
export const config = { debug: true };
// Ensure all importers are updated together
```

## Related Errors

- [Vite Build Error]({{< relref "/languages/javascript/vite-build-error" >}}) — rollup build failed
- [Vite SSR Error]({{< relref "/languages/javascript/vite-ssr-error" >}}) — SSR rendering failed
- [ESBuild Error]({{< relref "/languages/javascript/esbuild-error" >}}) — esbuild bundling error
