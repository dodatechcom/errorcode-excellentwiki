---
title: "Express Session Store Connection Error"
description: "Fix Express session errors when the session store (Redis, MongoDB, etc.) cannot connect or persist session data."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["session", "store", "redis", "mongodb", "express"]
weight: 5
---

## What This Error Means

When Express sessions are backed by an external store (Redis, MongoDB, database), a connection failure or misconfiguration causes session errors. The session middleware may throw an unhandled error, crash the process, or silently fail — causing users to lose their session data on every request.

## Common Causes

- Session store server (Redis, MongoDB) is not running or unreachable
- Connection string or credentials are incorrect
- Session store middleware is not initialized before routes that need sessions
- Session store has no error event handler configured
- Session serialization/deserialization fails due to data corruption

## How to Fix

### Configure Session Store with Error Handling

```javascript
const session = require('express-session');
const RedisStore = require('connect-redis').default;
const { createClient } = require('redis');

const redisClient = createClient({ url: 'redis://localhost:6379' });
redisClient.connect().catch(console.error);

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: false,
  cookie: { secure: true, maxAge: 86400000 }
}));

// Handle store errors
redisClient.on('error', (err) => {
  console.error('Redis session store error:', err);
});
```

### Add Fallback for Store Failures

```javascript
const session = require('express-session');

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: false
}));

// Graceful degradation: if store fails, use MemoryStore
app.use((err, req, res, next) => {
  if (err.code === 'ECONNREFUSED') {
    console.error('Session store unavailable, falling back to memory');
  }
  next(err);
});
```

### Use MongoDB Store Correctly

```javascript
const session = require('express-session');
const MongoStore = require('connect-mongo');

app.use(session({
  store: MongoStore.create({
    mongoUrl: 'mongodb://localhost:27017/myapp',
    ttl: 60 * 60 // 1 hour
  }),
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: false
}));
```

### Verify Session Data in Routes

```javascript
app.get('/dashboard', (req, res) => {
  if (!req.session || !req.session.userId) {
    return res.status(401).json({ error: 'Not authenticated' });
  }
  res.json({ userId: req.session.userId });
});
```

## Related Errors

- [Express JWT Error]({{< relref "/frameworks/express/express-jwt-error-v2" >}}) — token authentication failure
- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error-v2" >}}) — middleware chain issue
