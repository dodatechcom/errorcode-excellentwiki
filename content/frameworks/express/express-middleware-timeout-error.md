---
title: "[Solution] Express Middleware Timeout Error"
description: "Fix Express middleware timeout errors when requests hang and never receive a response from downstream services."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A middleware timeout error in Express occurs when a middleware function takes too long to complete, causing the client connection to hang or terminate. This typically happens when middleware calls external APIs, databases, or other slow resources without enforcing time limits.

## Common Causes

- Middleware calls an external HTTP service that never responds
- Database query inside middleware has no timeout configuration
- File system operations in middleware block the event loop
- Missing `next()` call in middleware causing the chain to stall
- Synchronous heavy computation blocking the Node.js event loop

## How to Fix

1. Add a timeout to outgoing HTTP requests inside middleware:

```javascript
const axios = require('axios');

app.use('/proxy', async (req, res, next) => {
  try {
    const response = await axios.get('https://api.example.com/data', {
      timeout: 5000
    });
    res.json(response.data);
  } catch (err) {
    if (err.code === 'ECONNABORTED') {
      return res.status(504).json({ error: 'Upstream service timed out' });
    }
    next(err);
  }
});
```

2. Set a database query timeout in your ORM or driver:

```javascript
// Using Knex
const result = await knex('users')
  .select('*')
  .where({ active: true })
  .timeout(3000, { cancel: true });

// Using Mongoose
const users = await User.find({ active: true })
  .maxTimeMS(3000);
```

3. Wrap async middleware with a timeout helper:

```javascript
function withTimeout(fn, ms) {
  return (req, res, next) => {
    const timer = setTimeout(() => {
      res.status(504).json({ error: 'Request timed out' });
    }, ms);
    res.on('finish', () => clearTimeout(timer));
    fn(req, res, next).catch(next);
  };
}

app.get('/slow', withTimeout(async (req, res) => {
  const data = await slowDatabaseQuery();
  res.json(data);
}, 10000));
```

## Examples

```javascript
// Problematic middleware that hangs when DB is slow
app.use(async (req, res, next) => {
  const user = await db.query('SELECT * FROM users WHERE id = ?', [req.userId]);
  req.user = user;
  next(); // Never reached if db.query hangs
});

// Fixed version with timeout
app.use(async (req, res, next) => {
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 3000);
    const user = await db.query('SELECT * FROM users WHERE id = ?', [req.userId], {
      signal: controller.signal
    });
    clearTimeout(timeout);
    req.user = user;
    next();
  } catch (err) {
    if (err.name === 'AbortError') {
      return res.status(504).json({ error: 'Database query timed out' });
    }
    next(err);
  }
});
```

```text
Error: Timeout of 5000ms exceeded
```
