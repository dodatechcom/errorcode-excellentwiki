---
title: "Vite HMR Failed to Update Module"
description: "Vite hot module replacement fails to update a module in the browser."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite HMR — Failed to Update Module

This error occurs when Vite's Hot Module Replacement (HMR) fails to update a module in the browser during development. The file change is detected but cannot be applied.

## Common Causes

- Module has runtime errors preventing HMR
- CSS module update failed
- Module boundary issues (non-HMR compatible code)
- WebSocket connection to dev server lost

## How to Fix

### Check Vite Dev Server Output

```bash
npx vite --debug
```

### Enable HMR Debug Logging

```javascript
// vite.config.js
export default defineConfig({
  server: {
    hmr: {
      overlay: true,
    },
  },
});
```

### Fix HMR-Incompatible Code

```javascript
// Use import.meta.hot for custom HMR handling
if (import.meta.hot) {
  import.meta.hot.accept('./module.js', (newModule) => {
    // Handle updated module
  });
}
```

### Ensure Module Has Clean Exports

```javascript
// Good for HMR
export function setup() { /* ... */ }
export function cleanup() { /* ... */ }

// Bad for HMR - side effects on import
setup();
```

### Restart Dev Server

```bash
# Kill existing process
pkill -f "vite"

# Restart
npx vite
```

### Fix WebSocket Connection

```javascript
export default defineConfig({
  server: {
    hmr: {
      host: 'localhost',
      port: 5173,
    },
  },
});
```

## Examples

```text
[vite] page reload src/App.vue (hot updated)
[vite] hmr update /src/App.vue failed
[vite] (client) TypeError: Cannot read property 'setup' of undefined
```

## Related Errors

- [Vite Dev Server Error]({{< relref "/tools/vite/vite-dev-server-error" >}}) — dev server issues
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
- [Vite CSS Error]({{< relref "/tools/vite/vite-css-error" >}}) — CSS processing failure
