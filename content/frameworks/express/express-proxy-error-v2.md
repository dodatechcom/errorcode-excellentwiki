---
title: "http-proxy-middleware Connection Error"
description: "Fix http-proxy-middleware errors when the proxy target is unreachable, times out, or returns unexpected responses."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["proxy", "http-proxy-middleware", "upstream", "gateway", "express"]
weight: 5
---

## What This Error Means

`http-proxy-middleware` forwards requests from your Express server to a backend service. Connection errors occur when the target server is down, unreachable, or returns an error. Without error handling, these errors surface as generic 502 Bad Gateway responses with no diagnostic information.

## Common Causes

- Target service is not running or crashed
- Target host/port is incorrect in the proxy configuration
- Network timeout — target is too slow to respond
- TLS/SSL issues when proxying to HTTPS targets
- Target server rejects the forwarded request

## How to Fix

### Configure Proxy with Error Handling

```javascript
const { createProxyMiddleware } = require('http-proxy-middleware');

app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3001',
  changeOrigin: true,
  onError: (err, req, res) => {
    console.error('Proxy error:', err.message);
    res.status(502).json({
      error: 'Bad Gateway',
      message: 'Backend service is unavailable'
    });
  },
  onProxyReq: (proxyReq, req, res) => {
    console.log(`Proxying: ${req.method} ${req.url}`);
  }
}));
```

### Add Timeout Configuration

```javascript
app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3001',
  changeOrigin: true,
  timeout: 30000, // 30 second timeout
  proxyTimeout: 30000,
  onError: (err, req, res) => {
    if (err.code === 'ECONNTIMEDOUT') {
      return res.status(504).json({ error: 'Gateway Timeout' });
    }
    res.status(502).json({ error: 'Proxy Error', detail: err.message });
  }
}));
```

### Handle HTTPS Targets

```javascript
app.use('/api', createProxyMiddleware({
  target: 'https://api.example.com',
  changeOrigin: true,
  secure: true, // Verify SSL certificates
  onError: (err, req, res) => {
    console.error('HTTPS proxy error:', err.code);
    res.status(502).json({ error: 'Backend service unreachable' });
  }
}));
```

### Log Proxy Activity for Debugging

```javascript
app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3001',
  changeOrigin: true,
  logLevel: 'debug',
  onProxyReq: (proxyReq) => {
    proxyReq.setHeader('X-Forwarded-For', proxyReq.getHeader('x-forwarded-for'));
  },
  onProxyRes: (proxyRes, req) => {
    console.log(`Proxy response: ${proxyRes.statusCode} for ${req.url}`);
  }
}));
```

## Related Errors

- [Express 404 Route Not Found]({{< relref "/frameworks/express/express-404-error-v2" >}}) — undefined route
- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error-v2" >}}) — cross-origin request blocked
