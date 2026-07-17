---
title: "[Solution] Express Proxy Error"
description: "Fix Express proxy errors. Resolve reverse proxy and upstream issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Express proxy error occurs when the application cannot forward requests to an upstream server. This can be caused by proxy misconfiguration or upstream unavailability.

## Common Causes

- Upstream server is not running
- Proxy target URL is incorrect
- SSL certificate verification fails
- Proxy timeout too short
- Missing proxy headers

## How to Fix

### Use http-proxy-middleware

```javascript
const { createProxyMiddleware } = require('http-proxy-middleware');

app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3001',
  changeOrigin: true,
}));
```

### Handle Proxy Errors

```javascript
app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3001',
  onError: (err, req, res) => {
    console.error('Proxy error:', err);
    res.status(502).json({ error: 'Bad gateway' });
  },
}));
```

### Configure SSL

```javascript
app.use('/api', createProxyMiddleware({
  target: 'https://api.example.com',
  changeOrigin: true,
  secure: false, // Disable SSL verification (dev only)
}));
```

### Set Timeout

```javascript
app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3001',
  proxyTimeout: 30000,
}));
```

## Examples

```javascript
// Example 1: Upstream not running
// ECONNREFUSED 127.0.0.1:3001
// Fix: start the upstream server

// Example 2: Wrong target
// Proxy error: getaddrinfo ENOTFOUND api.example.com
// Fix: verify target URL
```

## Related Errors

- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error" >}}) — middleware error
- [Express SSL Error]({{< relref "/frameworks/express/express-ssl-error" >}}) — SSL/TLS error
