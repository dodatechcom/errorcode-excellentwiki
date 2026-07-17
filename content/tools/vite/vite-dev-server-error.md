---
title: "Vite Dev Server Error"
description: "Vite development server fails to start or serve the application."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "dev-server", "development", "serve", "port"]
weight: 5
---

# Vite Dev Server Error

A Vite dev server error occurs when the development server cannot start, bind to the port, or serve the application. Vite uses esbuild for fast development serving.

## Common Causes

- Port already in use by another process
- Dev server configuration errors
- Missing Vite dependencies
- Proxy configuration errors
- Certificate issues for HTTPS

## How to Fix

### Check Port Availability

```bash
lsof -i :5173
# Vite default port is 5173
```

### Change Dev Server Port

```javascript
// vite.config.js
export default defineConfig({
  server: {
    port: 3000,
    // Or allow random port
    port: true,
  },
});
```

### Fix Proxy Configuration

```javascript
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:3001',
        changeOrigin: true,
      },
    },
  },
});
```

### Use HTTPS with Certificate

```javascript
export default defineConfig({
  server: {
    https: {
      cert: fs.readFileSync('./cert.pem'),
      key: fs.readFileSync('./key.pem'),
    },
  },
});
```

### Check Vite Dependencies

```bash
npm ls vite esbuild
```

### Enable Detailed Error Output

```bash
npx vite --debug
```

## Examples

```bash
npx vite
Port 5173 is already in use

# Fix:
lsof -ti:5173 | xargs kill -9
# Or change port in vite.config.js
```

## Related Errors

- [Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — build failure
- [HMR Error]({{< relref "/tools/vite/vite-hmr-error" >}}) — HMR failure
- [Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
