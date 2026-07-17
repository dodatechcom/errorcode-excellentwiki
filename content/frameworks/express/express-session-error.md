---
title: "[Solution] Express Session Error — session error"
description: "Fix Express session errors. Resolve session storage and configuration issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["session", "cookie", "store", "storage", "express"]
weight: 5
---

An Express session error occurs when sessions cannot be created, stored, or retrieved. This can break authentication and user state management.

## Common Causes

- Session store not configured or misconfigured
- Redis/MongoDB session store connection failed
- Secret key not set or too weak
- Cookie settings incompatible with the environment
- Session store middleware not registered

## How to Fix

### Configure Session Middleware

```javascript
const session = require('express-session');

app.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: false,
  cookie: { secure: false, maxAge: 86400000 }
}));
```

### Use Redis Session Store

```javascript
const RedisStore = require('connect-redis').default;
const redis = require('redis');

const redisClient = redis.createClient();

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: 'your-secret',
  resave: false,
  saveUninitialized: false,
}));
```

### Use MongoDB Session Store

```javascript
const MongoStore = require('connect-mongo');

app.use(session({
  store: MongoStore.create({ mongoUrl: 'mongodb://localhost:27017/sessions' }),
  secret: 'your-secret',
}));
```

### Set Secure Cookie in Production

```javascript
cookie: {
  secure: process.env.NODE_ENV === 'production',
  httpOnly: true,
  sameSite: 'lax',
}
```

## Examples

```javascript
// Example 1: Session not persisting
// Fix: configure session store

// Example 2: Cookie not set
// Fix: ensure session middleware is before routes
app.use(session({...}));
app.use('/api', apiRouter); // Must come after session
```

## Related Errors

- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error" >}}) — middleware error
- [Express JWT Error]({{< relref "/frameworks/express/express-jwt-error" >}}) — JWT verification error
