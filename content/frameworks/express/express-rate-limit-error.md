---
title: "[Solution] Express Rate Limit Exceeded"
description: "Fix Express rate limit exceeded errors. Resolve request throttling issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A rate limit exceeded error occurs when a client sends too many requests within a time window. Express returns 429 Too Many Requests.

## Common Causes

- Client exceeding configured request limit
- Rate limit window too short
- Missing rate limit configuration for specific routes
- Multiple clients sharing same IP (NAT/proxy)
- Rate limit store not configured for distributed systems

## How to Fix

### Configure Rate Limiter

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests, please try again later.',
});

app.use('/api/', limiter);
```

### Custom Rate Limit Messages

```javascript
app.use('/api/', rateLimit({
  windowMs: 60 * 1000,
  max: 10,
  message: { error: 'Rate limit exceeded. Wait 1 minute.' },
  standardHeaders: true,
  legacyHeaders: false,
}));
```

### Use Redis Store for Distributed

```javascript
const RedisStore = require('rate-limit-redis');
const redis = require('redis');

app.use(rateLimit({
  store: new RedisStore({ sendCommand: (...args) => redisClient.sendCommand(args) }),
  windowMs: 15 * 60 * 1000,
  max: 100,
}));
```

### Skip Rate Limit for Specific Routes

```javascript
app.use('/health', (req, res, next) => next());
app.use('/api/', limiter);
```

## Examples

```javascript
// Example 1: Default limits too strict
// 429 Too Many Requests
// Fix: increase max or windowMs

// Example 2: Different limits per route
app.use('/api/auth', rateLimit({ windowMs: 15*60*1000, max: 5 }));
app.use('/api/data', rateLimit({ windowMs: 15*60*1000, max: 100 }));
```

## Related Errors

- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error" >}}) — middleware error
- [Express JWT Error]({{< relref "/frameworks/express/express-jwt-error" >}}) — JWT verification error
