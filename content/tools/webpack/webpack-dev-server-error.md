---
title: "Webpack Dev Server Error"
description: "Webpack development server fails to start or serve the application."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Dev Server Error

A Webpack dev server error occurs when `webpack-dev-server` cannot start, bind to the port, or serve the application during development.

## Common Causes

- Port already in use by another process
- Dev server configuration errors
- Missing webpack-dev-server dependency
- Proxy configuration errors
- Certificate issues for HTTPS

## How to Fix

### Check Port Availability

```bash
lsof -i :8080
# Kill process or use different port
```

### Change Dev Server Port

```javascript
// webpack.config.js
module.exports = {
  devServer: {
    port: 3000,
    // Or allow random port
    port: 0,
  },
};
```

### Install webpack-dev-server

```bash
npm install --save-dev webpack-dev-server
```

### Fix Proxy Configuration

```javascript
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  },
};
```

### Use HTTPS with Certificate

```javascript
module.exports = {
  devServer: {
    https: true,
    cert: fs.readFileSync('./cert.pem'),
    key: fs.readFileSync('./key.pem'),
  },
};
```

### Check for Configuration Errors

```bash
npx webpack serve --stats-error-details
```

## Examples

```bash
npx webpack serve
[webpack-dev-server] Error: listen EADDRINUSE: address already in use :::8080

# Fix:
lsof -ti:8080 | xargs kill -9
# Or change port
npx webpack serve --port 3000
```

## Related Errors

- [Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — build failure
- [Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
- [Hot Reload Error]({{< relref "/tools/webpack/webpack-hot-reload-error" >}}) — HMR failure
