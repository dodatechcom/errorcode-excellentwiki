---
title: "Express 404 Route Not Found"
description: "Fix Express 404 errors when routes are not registered or the client requests an undefined endpoint."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An Express 404 error occurs when a client sends a request to a URL that has no matching route handler. By default, Express returns a generic HTML response with "Cannot GET /path". Without a proper catch-all handler, clients receive unhelpful error messages and API consumers cannot parse the response.

## Common Causes

- Route path has a typo or mismatched HTTP method (GET vs POST)
- Route is defined but never mounted on the app
- Client sends a request before the route file is imported
- Dynamic route parameter syntax is incorrect (e.g., `:id` vs `:idd`)
- No catch-all 404 handler for undefined routes

## How to Fix

### Add a Catch-All 404 Handler

```javascript
// Place this AFTER all your routes
app.use((req, res, next) => {
  res.status(404).json({
    error: 'Not Found',
    message: `Route ${req.method} ${req.originalUrl} does not exist`
  });
});
```

### Verify Route Registration Order

```javascript
const apiRouter = require('./routes/api');

// Make sure router is mounted before the 404 handler
app.use(express.json());
app.use('/api', apiRouter);

// 404 handler comes last
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});
```

### Use Express Router Correctly

```javascript
// router.js
const express = require('express');
const router = express.Router();

router.get('/users', (req, res) => {
  res.json({ users: [] });
});

module.exports = router;

// app.js
const apiRouter = require('./routes/api');
app.use('/api', apiRouter); // Requests go to /api/users
```

### Log Missing Routes for Debugging

```javascript
app.use((req, res, next) => {
  console.warn(`404: ${req.method} ${req.originalUrl} from ${req.ip}`);
  res.status(404).json({ error: 'Not Found' });
});
```

## Related Errors

- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error-v2" >}}) — middleware not passing control
- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error-v2" >}}) — cross-origin request blocked
