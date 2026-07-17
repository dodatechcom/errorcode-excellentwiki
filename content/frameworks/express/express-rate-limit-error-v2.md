---
title: "Rate Limit Exceeded in Express"
description: "Fix Express rate limit errors when clients exceed request thresholds set by the express-rate-limit middleware."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

When a client sends too many requests within a defined time window, the `express-rate-limit` middleware responds with a `429 Too Many Requests` status. This is intentional protection, but misconfiguration can block legitimate users or fail to protect against abuse.

## Common Causes

- Rate limit window or max is too restrictive for normal usage
- Shared IP addresses (NAT, proxies) cause all users to share a limit
- No rate limit headers sent, so clients cannot back off
- Rate limiter not reset between deployments or testing
- Default in-memory store used in clustered environments

## How to Fix

### Configure Rate Limiting Per Route

```javascript
const rateLimit = require('express-rate-limit');

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: 'Too many requests, please try again later' }
});

app.use('/api', apiLimiter);

// Stricter limit for auth routes
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // 5 attempts per 15 minutes
  message: { error: 'Too many login attempts' }
});

app.use('/auth/login', authLimiter);
```

### Use Redis Store for Clusters

```javascript
const rateLimit = require('express-rate-limit');
const RedisStore = require('rate-limit-redis');
const { createClient } = require('redis');

const redisClient = createClient({ url: 'redis://localhost:6379' });
redisClient.connect();

const limiter = rateLimit({
  store: new RedisStore({ sendCommand: (...args) => redisClient.sendCommand(args) }),
  windowMs: 15 * 60 * 1000,
  max: 100
});

app.use('/api', limiter);
```

### Handle Rate Limit Errors in Client

```javascript
// Client-side retry with backoff
app.use((err, req, res, next) => {
  if (err.status === 429) {
    const retryAfter = err.headers['retry-after'] || 60;
    return res.status(429).json({
      error: 'Rate limit exceeded',
      retryAfter: parseInt(retryAfter)
    });
  }
  next(err);
});
```

### Customize Key Generation

```javascript
const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 30,
  keyGenerator: (req) => {
    return req.user?.id || req.ip; // Use user ID if authenticated
  }
});
```

## Related Errors

- [Express 404 Route Not Found]({{< relref "/frameworks/express/express-404-error-v2" >}}) — undefined route
- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error-v2" >}}) — cross-origin request blocked
