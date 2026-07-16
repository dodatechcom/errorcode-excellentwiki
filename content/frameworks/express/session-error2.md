---
title: "Session not found"
description: "Express session middleware fails because the session store or session ID is missing or invalid"
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["session", "cookie", "store", "middleware"]
weight: 5
---

This error occurs when Express session middleware cannot find or deserialize a session, typically because the session store is unavailable, the session cookie is missing, or the session ID is invalid.

## Common Causes

- Session store (e.g. Redis, database) is not running or misconfigured
- Session cookie not sent with the request (e.g. `SameSite` or `Domain` mismatch)
- Session secret is not set or has changed, invalidating existing sessions
- Session ID in the cookie does not match any session in the store

## How to Fix

1. Configure sessions with a secret and store:

```javascript
const session = require('express-session');
const RedisStore = require('connect-redis').default;
const redis = require('redis');

const client = redis.createClient({ url: 'redis://localhost:6379' });
client.connect();

app.use(session({
  store: new RedisStore({ client }),
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: process.env.NODE_ENV === 'production',
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000
  }
}));
```

2. Ensure the session store is running and accessible:

```bash
redis-cli ping
# PONG
```

3. Use a stable session secret (never change in production):

```javascript
app.use(session({
  secret: process.env.SESSION_SECRET, // from environment
  // ...
}));
```

## Examples

```javascript
app.get('/dashboard', (req, res) => {
  if (!req.session.userId) {
    return res.redirect('/login'); // session not found or expired
  }
  res.json({ user: req.session.userId });
});
```

```text
Error: Failed to deserialize user out of session
```

## Related Errors

- [Rate limit exceeded]({{< relref "/frameworks/express/rate-limit" >}})
