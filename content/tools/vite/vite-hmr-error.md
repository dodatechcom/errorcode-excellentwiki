---
title: "Vite HMR Error — Update Failed"
description: "Vite Hot Module Replacement fails to update modules in the development server."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "hmr", "hot-module", "development", "update"]
weight: 5
---

# Vite HMR Error — Update Failed

A Vite HMR error occurs when the Hot Module Replacement system cannot update modules in the development server. The page may need a full reload instead of an in-place update.

## Common Causes

- Module cannot be hot-replaced (non-replaceable exports)
- WebSocket connection to dev server lost
- Module has side effects preventing replacement
- Code syntax error prevents HMR update

## How to Fix

### Check Vite Dev Server Connection

```bash
# Ensure dev server is running
npx vite
```

### Add HMR Accept Handler

```javascript
// In modules that support HMR
if (import.meta.hot) {
  import.meta.hot.accept('./utils', () => {
    // Module updated
  });
  import.meta.hot.dispose(() => {
    // Cleanup before replacement
  });
}
```

### Enable HMR in Config

```javascript
// vite.config.js
export default defineConfig({
  server: {
    hmr: true,
    // Specify WebSocket port
    hmr: {
      port: 24678,
    },
  },
});
```

### Fix Non-Replaceable Exports

```javascript
// Only default exports can be hot-replaced
// Convert named exports to default export
export default { fn1, fn2 };
```

### Check Browser Console for Errors

```javascript
// Look for HMR error messages in browser console
// Fix the underlying module error first
```

## Examples

```javascript
// Browser console error
[vite] hmr update failed: Error: Aborted because there is no acceptance handler
for ./src/utils.js

// Fix: add HMR accept handler
if (import.meta.hot) {
  import.meta.hot.accept('./utils', () => {});
}
```

## Related Errors

- [Dev Server Error]({{< relref "/tools/vite/dev-server-error" >}}) — dev server issues
- [Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — build failure
