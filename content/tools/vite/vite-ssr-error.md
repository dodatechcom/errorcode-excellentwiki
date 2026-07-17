---
title: "Vite SSR Error — Server-Side Rendering Failed"
description: "Vite SSR build or runtime fails during server-side rendering."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "ssr", "server-side", "rendering", "node"]
weight: 5
---

# Vite SSR Error — Server-Side Rendering Failed

A Vite SSR error occurs when the server-side rendering build or runtime fails. This can happen during SSR bundle generation or when the server attempts to render the application.

## Common Causes

- Browser-only APIs used in SSR code
- Missing SSR-compatible dependencies
- Incorrect SSR build configuration
- Module resolution differences between client and server

## How to Fix

### Configure SSR Build

```javascript
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        client: resolve(__dirname, 'index.html'),
        server: resolve(__dirname, 'src/entry-server.js'),
      },
    },
  },
  ssr: {
    // Externalize node-only modules
    external: ['fs', 'path'],
    noExternal: ['some-esm-package'],
  },
});
```

### Guard Browser-Only Code

```javascript
// Only access window/document on the client side
if (typeof window !== 'undefined') {
  // Browser-only code
}
```

### Check SSR Compatibility

```bash
npm run build -- --mode ssr
# Or use Vite's built-in SSR support
npx vite build --ssr src/entry-server.js
```

### Fix Module Resolution

```javascript
export default defineConfig({
  resolve: {
    conditions: ['import', 'module', 'browser', 'default'],
  },
});
```

## Examples

```bash
npx vite build --ssr src/entry-server.js
error: 'document' is not defined
at /src/app.js:10:5

# Fix: guard browser-only code
if (typeof document !== 'undefined') {
  document.querySelector('#app');
}
```

## Related Errors

- [Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — build failure
- [Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
