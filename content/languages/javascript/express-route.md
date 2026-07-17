---
title: "[Solution] Express Route Not Found 404 Error Fix"
description: "Fix Express 404 route not found errors. Handle missing routes, route ordering, and serve proper 404 responses."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["express", "404", "route", "not-found", "middleware"]
weight: 5
---

# Express Route — not found 404

This error occurs when an Express application receives a request for a route that hasn't been defined. It can also occur when route ordering causes a catch-all to intercept specific routes.

## What This Error Means

Common error messages:

- `Cannot GET /path`
- `404 Not Found`
- `NotFoundError: Not Found`

Express returns 404 for undefined routes. Without a custom 404 handler, the default response is generic.

## Common Causes

```javascript
// Cause 1: Route not defined
app.get('/api/users', handler);
// GET /api/products → 404

// Cause 2: Wrong HTTP method
app.get('/api/users', handler);
app.post('/api/users', handler);
// GET /api/users with POST → 404

// Cause 3: Route ordering issue
app.get('/api/:id', handler);
app.get('/api/users', handler); // never reached - :id matches first

// Cause 4: Missing route definition
// App has routes but no catch-all or 404 handler
```

## How to Fix

### Fix 1: Add 404 handler at the end

```javascript
app.get('/api/users', handler);
app.post('/api/users', handler);

// 404 handler - must be after all routes
app.use((req, res) => {
  res.status(404).json({ error: `Route ${req.method} ${req.path} not found` });
});
```

### Fix 2: Fix route ordering

```javascript
// Wrong - /:id matches /users too
app.get('/api/:id', handler);
app.get('/api/users', handler);

// Correct - specific routes first
app.get('/api/users', handler);
app.get('/api/:id', handler); // only matches after /api/:id
```

### Fix 3: Handle all HTTP methods

```javascript
app.all('/api/users', (req, res) => {
  switch (req.method) {
    case 'GET': return handleGet(req, res);
    case 'POST': return handlePost(req, res);
    default: return res.status(405).json({ error: 'Method not allowed' });
  }
});
```

### Fix 4: Use router for modular routes

```javascript
const usersRouter = express.Router();
usersRouter.get('/', listUsers);
usersRouter.post('/', createUser);
usersRouter.get('/:id', getUser);

app.use('/api/users', usersRouter);
```

## Examples

```javascript
// This triggers 404
const app = express();
app.get('/api/data', (req, res) => res.json({ data: 'ok' }));

// No 404 handler defined
// GET /api/missing → "Cannot GET /api/missing"

// Fix: add 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});
```

## Related Errors

- [Express Params]({{< relref "/languages/javascript/express-params" >}}) — params undefined
- [Express Middleware]({{< relref "/languages/javascript/express-middleware" >}}) — middleware error
- [Express Session]({{< relref "/languages/javascript/express-session" >}}) — session error
