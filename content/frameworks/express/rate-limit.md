---
title: "Too many requests (rate limit)"
description: "Express returns HTTP 429 when a client exceeds the configured rate limit"
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["rate-limit", "throttle", "429", "middleware"]
weight: 5
---

This error occurs when Express rate limiting middleware rejects a request because the client has exceeded the allowed number of requests within a given time window.

## Common Causes

- Client sending too many requests per second/minute
- Rate limit configured too aggressively for the use case
- Multiple clients sharing the same IP address (e.g. behind a proxy)
- Missing rate limit headers in client responses

## How to Fix

1. Use `express-rate-limit` middleware:

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  standardHeaders: true,
  legacyHeaders: false,
});

app.use('/api/', limiter);
```

2. Configure per-route rate limits:

```javascript
const authLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 5,
  message: 'Too many login attempts, try again later'
});

app.post('/login', authLimiter, (req, res) => {
  // login handler
});
```

3. Use a custom key generator for per-user limits:

```javascript
const userLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 50,
  keyGenerator: (req) => req.user?.id || req.ip
});

app.use('/api/', userLimiter);
```

## Examples

```javascript
// Client making rapid requests
for (let i = 0; i < 200; i++) {
  fetch('/api/data'); // After 100 requests: 429 Too Many Requests
}
```

```text
HTTP/1.1 429 Too Many Requests
Retry-After: 300
{"message": "Too many requests, please try again later."}
```

## Related Errors

- [Cannot GET /X]({{< relref "/frameworks/express/route-not-found" >}})
