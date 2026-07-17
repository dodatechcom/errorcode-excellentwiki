---
title: "[Solution] Vite: HMR Update Failed Fix"
description: "Fix Vite HMR (Hot Module Replacement) errors during development. Handle failed updates, disconnected WebSocket, and stale module cache."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite: HMR Update Failed

This error occurs when Vite's Hot Module Replacement system fails to apply a code change to the running application in the browser. The dev server loses sync with the client and requires a page reload.

## What This Error Means

Common error messages:

- `[vite] hmr update /src/App.tsx failed`
- `[vite] Failed to reload /src/utils.ts. This could be due to syntax errors or importing non-existent modules.`
- `[vite] WebSocket connection lost. Reconnecting...`
- `[vite] client error: ReferenceError: XYZ is not defined after HMR`

HMR works by sending a small update payload over a WebSocket connection. The browser-side runtime then swaps the changed module. If the swap fails, Vite falls back to a full page reload or shows an error.

## Common Causes

```javascript
// Cause 1: Syntax error introduced in edited file
export const config = {
  port: 3000  // missing comma causes parse error
}

// Cause 2: Top-level side effects that break on re-execution
document.title = 'My App'; // runs again on every HMR update

// Cause 3: Module-level state gets reset
let connection = establishWebSocket(); // lost on HMR

// Cause 4: CSS imported via JS with invalid syntax
import './styles.css'; // file contains unsupported @import

// Cause 5: WebSocket timeout due to slow machine or large payload
```

## How to Fix

### Fix 1: Use HMR-safe module patterns

```javascript
// ❌ Bad: top-level side effect
console.log('module loaded');

// ✅ Good: use import.meta.hot
if (import.meta.hot) {
  import.meta.hot.accept();
}
```

### Fix 2: Preserve module state across HMR updates

```javascript
// Preserve state on hot reload
let state = { count: 0 };

if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    // Apply new module without losing state
    if (newModule) {
      newModule.setState(state);
    }
  });
}

export function setState(s) {
  state = s;
}
```

### Fix 3: Use `import.meta.hot.dispose` for cleanup

```javascript
const listener = (e) => console.log(e);

window.addEventListener('message', listener);

if (import.meta.hot) {
  import.meta.hot.dispose(() => {
    window.removeEventListener('message', listener);
  });
}
```

### Fix 4: Increase WebSocket timeout

```javascript
// vite.config.js
export default defineConfig({
  server: {
    hmr: {
      timeout: 60000, // 60 seconds
    },
  },
});
```

### Fix 5: Disable HMR for problematic files

```javascript
// vite.config.js
export default defineConfig({
  server: {
    watch: {
      ignored: ['**/generated/**', '**/node_modules/**'],
    },
  },
});
```

## Examples

```bash
[src/App.tsx] hmr update /src/App.tsx
[src/App.tsx] hmr update /src/App.tsx failed
```

```
[vite] hmr update failed: Error: Cannot hot reload "solid-js/web"
Try deleting the cache directory: rm -rf node_modules/.vite
```

## Related Errors

- [Vite Build Error]({{< relref "/languages/javascript/vite-build-error" >}}) — production build failed
- [Vite Build Error V2]({{< relref "/languages/javascript/vite-build-error-v2" >}}) — Rollup build failed
- [WebSocket Timeout]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket timeout
