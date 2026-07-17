---
title: "[Solution] Express Session Error Fix"
description: "Fix Express session errors including session store issues, cookie configuration, and session serialization problems."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["express", "session", "cookie", "store", "express-session"]
weight: 5
---

# Express Session Error

This error occurs when Express sessions fail due to store issues, cookie misconfiguration, or serialization problems.

## What This Error Means

Common error messages:

- `Error: Unable to serialize session`
- `Error: Session store error`
- `Warning: connect.session() MemoryStore not designed`

The `express-session` middleware manages sessions via stores (memory, Redis, database).

## Common Causes

```javascript
// Cause 1: MemoryStore in production
app.use(session({
  secret: 'secret',
  resave: false,
  saveUninitialized: false,
}));

// Cause 2: Session store not available
const RedisStore = require('connect-redis').default;
app.use(session({
  store: new RedisStore({ client: redisClient }), // redisClient not connected
}));

// Cause 3: Non-serializable session data
req.session.data = someFunction; // functions can't be serialized

// Cause 4: Cookie configuration error
app.use(session({
  cookie: { secure: true }, // requires HTTPS
}));
```

## How to Fix

### Fix 1: Use external session store

```javascript
const RedisStore = require('connect-redis').default;
const { createClient } = require('redis');

const redisClient = createClient({ url: 'redis://localhost:6379' });
redisClient.connect();

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: 'your-secret',
  resave: false,
  saveUninitialized: false,
}));
```

### Fix 2: Configure cookies properly

```javascript
app.use(session({
  secret: 'your-secret',
  cookie: {
    secure: process.env.NODE_ENV === 'production',
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000, // 1 day
    sameSite: 'lax',
  },
}));
```

### Fix 3: Only serialize plain objects

```javascript
// Wrong
req.session.user = {
  id: 1,
  getRole: () => 'admin', // can't serialize
};

// Correct
req.session.user = {
  id: 1,
  role: 'admin', // plain value
};
```

### Fix 4: Handle session errors

```javascript
app.use(session({
  secret: 'secret',
  store: new RedisStore({ client: redisClient }),
}));

app.use((err, req, res, next) => {
  if (err.code === 'EBADSESSION') {
    return res.status(500).json({ error: 'Session error' });
  }
  next(err);
});
```

## Examples

```javascript
// This triggers session error
app.use(session({
  store: new RedisStore({ client: null }), // no client
}));

// Fix: connect Redis first
const client = createClient();
client.connect().then(() => {
  app.use(session({
    store: new RedisStore({ client }),
    secret: 'secret',
  }));
});
```

## Related Errors

- [Express Middleware]({{< relref "/languages/javascript/express-middleware" >}}) — middleware error
- [Passport Error]({{< relref "/languages/javascript/passport-error" >}}) — authentication failed
- [JWT Error]({{< relref "/languages/javascript/jsonwebtoken-error" >}}) — token error
