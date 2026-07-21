---
title: "[Solution] Express Route Not Found 404 Error"
description: "Fix Express 404 route not found errors when the client receives a 404 for a valid endpoint."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A 404 route not found error in Express occurs when a request reaches the server but no route matches the URL path. This can happen even for routes you believe are properly defined.

## Common Causes

- Route path typo or case mismatch in the URL
- HTTP method mismatch (GET vs POST)
- Route registered on a router that is not mounted
- Middleware sends response before the route handler executes
- Trailing slash inconsistency between client and server

## How to Fix

1. Add a catch-all 404 handler after all route definitions:

```javascript
app.use('/api', apiRouter);

// Must be after all routes
app.use((req, res) => {
  res.status(404).json({ error: `Route ${req.method} ${req.url} not found` });
});
```

2. Normalize route paths and ensure consistent mounting:

```javascript
const router = express.Router();

router.get('/users', (req, res) => {
  res.json({ users: [] });
});

// Mount with or without trailing slash
app.use('/api', router);

// Accessible at both /api/users and /api/users/
```

3. Log unmatched routes for debugging:

```javascript
app.use((req, res, next) => {
  console.log(`404: ${req.method} ${req.originalUrl}`);
  res.status(404).json({ error: 'Not found' });
});
```

## Examples

```javascript
// Router mounted but path doesn't match
const adminRouter = express.Router();
adminRouter.get('/dashboard', handler);
app.use('/admin', adminRouter);

// Works: GET /admin/dashboard
// Fails: GET /admin/Dashboard (case sensitive)
// Fails: GET /admin/dashboard/ (trailing slash)
```

```text
Cannot GET /api/users
```
