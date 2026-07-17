---
title: "Webpack DevServer Connection Error"
description: "Webpack dev server fails to start or accept connections."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webpack", "dev-server", "connection", "port", "proxy"]
weight: 5
---

# Webpack DevServer — Connection Error

This error occurs when the webpack dev server fails to start, bind to a port, or accept connections. The development server cannot serve assets to the browser.

## Common Causes

- Port already in use by another process
- Proxy target server not running
- Invalid host or port configuration
- Firewall blocking the port
- Invalid HTTPS certificate

## How to Fix

### Check Port Availability

```bash
lsof -i :8080
# Kill existing process if needed
kill -9 <PID>
```

### Configure Dev Server

```javascript
// webpack.config.js
module.exports = {
  devServer: {
    port: 8080,
    host: 'localhost',
    open: true,
  },
};
```

### Use Different Port

```bash
npx webpack serve --port 3000
```

### Configure Proxy

```javascript
devServer: {
  proxy: {
    '/api': {
      target: 'http://localhost:3001',
      changeOrigin: true,
    },
  },
},
```

### Allow Port Through Firewall

```bash
# Linux
sudo ufw allow 8080

# macOS
sudo pfctl -f /etc/pf.conf
```

### Fix HTTPS Issues

```javascript
devServer: {
  https: true,
  cert: fs.readFileSync('./cert.pem'),
  key: fs.readFileSync('./key.pem'),
},
```

## Examples

```text
[webpack-dev-server] Project is running at:
[webpack-dev-server] Loopback: http://localhost:8080/
Error: listen EADDRINUSE: address already in use :::8080
```

## Related Errors

- [Webpack Hot Reload Error]({{< relref "/tools/webpack/webpack-hot-reload-error" >}}) — HMR failures
- [Webpack Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
- [Webpack Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
