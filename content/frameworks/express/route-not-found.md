---
title: "Cannot GET /X (404 route not found)"
description: "Express returns 404 when no route handler matches the request URL"
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["routing", "404", "not-found", "middleware"]
weight: 5
---

This error occurs when Express cannot find a route handler that matches the incoming request method and URL. It returns a plain 404 response by default.

## Common Causes

- Route not registered for the given URL path
- HTTP method mismatch (e.g. GET instead of POST)
- Route path typo or missing prefix (e.g. `/api/user` vs `/api/users`)
- Middleware blocking the request before it reaches the route

## How to Fix

1. Add a global 404 handler at the end of all routes:

```javascript
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});
```

2. Verify routes are registered before the 404 handler:

```javascript
app.get('/api/users', (req, res) => {
  res.json([]);
});

app.post('/api/users', (req, res) => {
  res.status(201).json({ id: 1 });
});

// This MUST come after all routes
app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});
```

3. List all registered routes for debugging:

```javascript
function printRoutes(app) {
  app._router.stack.forEach((middleware) => {
    if (middleware.route) {
      console.log(`${Object.keys(middleware.route.methods).join(', ')} ${middleware.route.path}`);
    }
  });
}
```

## Examples

```javascript
// Trying to GET a route that is only registered for POST
app.post('/api/users', (req, res) => {
  res.json({ id: 1 });
});

// Browser navigates to /api/users → 404
```

```text
Cannot GET /api/users
```

## Related Errors

- [CORS policy error]({{< relref "/frameworks/express/cors-error" >}})
