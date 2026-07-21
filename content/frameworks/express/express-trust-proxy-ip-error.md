---
title: "[Solution] Express Trust Proxy Error"
description: "Fix Express trust proxy errors when client IP and protocol are incorrect behind a reverse proxy."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A trust proxy error in Express occurs when the application runs behind a reverse proxy like nginx or AWS ELB but `trust proxy` is not configured, causing `req.ip`, `req.protocol`, and `req.hostname` to return the proxy's values instead of the client's.

## Common Causes

- `trust proxy` not set when behind a load balancer
- `req.ip` returns the proxy IP instead of the client IP
- `X-Forwarded-For` header is trusted from untrusted sources
- Rate limiting based on proxy IP instead of client IP
- HTTPS detection fails because `X-Forwarded-Proto` is not read

## How to Fix

1. Configure trust proxy based on your infrastructure:

```javascript
// Trust first proxy (single proxy setup)
app.set('trust proxy', 1);

// Trust specific subnets
app.set('trust proxy', ['10.0.0.0/8', '172.16.0.0/12']);

// Trust all proxies (use with caution)
app.set('trust proxy', true);
```

2. Use trusted proxy settings with rate limiting:

```javascript
app.set('trust proxy', 1);

const rateLimit = require('express-rate-limit');
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  keyGenerator: (req) => req.ip // Now uses real client IP
});

app.use(limiter);
```

3. Detect HTTPS behind a load balancer:

```javascript
app.set('trust proxy', 1);

app.use((req, res, next) => {
  if (req.secure || req.headers['x-forwarded-proto'] === 'https') {
    return next();
  }
  res.redirect(`https://${req.headers.host}${req.url}`);
});
```

## Examples

```javascript
// Bug: req.ip returns proxy IP (10.0.0.1) instead of client
app.set('trust proxy', false);

app.get('/api/info', (req, res) => {
  res.json({ ip: req.ip }); // Returns proxy IP
});

// Fixed: trust the proxy
app.set('trust proxy', 1);

app.get('/api/info', (req, res) => {
  res.json({ ip: req.ip }); // Returns real client IP
});
```

```text
req.ip returns 10.0.0.1 instead of 203.0.113.50
```
