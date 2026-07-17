---
title: "[Solution] Express 404 Not Found"
description: "Fix Express 404 Not Found errors. Resolve route and endpoint not found issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Express 404 error occurs when no route matches the requested URL. Express cannot find a handler for the HTTP method and path combination.

## Common Causes

- Route path does not match the URL
- HTTP method mismatch (GET vs POST)
- Route defined after the 404 handler
- Typos in route path or URL
- Route is behind authentication middleware

## How to Fix

### Define 404 Handler Last

```javascript
app.use('/api', apiRouter);

// 404 handler must come after all routes
app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});
```

### Check Route Definitions

```javascript
app.get('/api/users', (req, res) => {
  res.json(users);
});
// Request to /api/user (missing 's') -> 404
```

### Use Router Properly

```javascript
const router = express.Router();
router.get('/users', handler);
app.use('/api', router);
// Accessible at /api/users
```

### Debug Routes

```javascript
console.log('Registered routes:');
app._router.stack.forEach((r) => {
  if (r.route) console.log(r.route.path, Object.keys(r.route.methods));
});
```

## Examples

```javascript
// Example 1: Route not found
GET /api/users/123
// 404 Not Found
// Fix: add route app.get('/api/users/:id', handler)

// Example 2: Wrong method
app.post('/api/data', handler);
// GET /api/data -> 404
// Fix: add GET handler or check client method
```

## Related Errors

- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error" >}}) — middleware error
- [Express Validation Error]({{< relref "/frameworks/express/express-validation-error" >}}) — validation error
