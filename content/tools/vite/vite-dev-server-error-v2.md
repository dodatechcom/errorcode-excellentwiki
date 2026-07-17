---
title: "Vite Dev Middleware Error"
description: "Vite development server middleware encounters an error."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "dev", "middleware", "server", "proxy"]
weight: 5
---

# Vite Dev — Middleware Error

This error occurs when Vite's development server middleware encounters an error. The middleware pipeline fails to process a request correctly.

## Common Causes

- Proxy middleware misconfigured
- Custom middleware throws an error
- Request handler timeout
- Middleware ordering conflict

## How to Fix

### Check Dev Server Configuration

```javascript
// vite.config.js
export default defineConfig({
  server: {
    port: 3000,
    host: 'localhost',
  },
});
```

### Configure Proxy Correctly

```javascript
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:3001',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
});
```

### Add Error Handling

```javascript
export default defineConfig({
  server: {
    middlewareMode: false,
  },
  plugins: [
    {
      name: 'middleware-error-handler',
      configureServer(server) {
        server.middlewares.use((err, req, res, next) => {
          console.error('Middleware error:', err);
          res.statusCode = 500;
          res.end('Internal Server Error');
        });
      },
    },
  ],
});
```

### Check Proxy Target Server

```bash
# Ensure target server is running
curl http://localhost:3001/api/health
```

### Fix WebSocket Proxy

```javascript
export default defineConfig({
  server: {
    proxy: {
      '/socket': {
        target: 'ws://localhost:3001',
        ws: true,
      },
    },
  },
});
```

## Examples

```text
[vite] Internal server error: connect ECONNREFUSED 127.0.0.1:3001
  at TCPConnectWrap.afterConnect [as oncomplete]
```

## Related Errors

- [Vite Dev Server Error]({{< relref "/tools/vite/vite-dev-server-error" >}}) — dev server issues
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
- [Vite HMR Error]({{< relref "/tools/vite/vite-hmr-error" >}}) — HMR failures
