---
title: "[Solution] Express Async Handler Error"
description: "Fix Express async handler errors by catching rejected promises in route handlers and middleware."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An async handler error in Express occurs when a route handler or middleware returns a rejected promise that is never caught. Express does not automatically catch promise rejections in async functions, so unhandled rejections crash the process or hang requests.

## Common Causes

- Async route handler throws without try/catch
- `next(err)` not called in async middleware
- Express version below 5 does not handle async rejections
- Database or API call inside async handler throws an error
- Missing error handling wrapper for async functions

## How to Fix

1. Use an async handler wrapper to catch rejections:

```javascript
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/api/users/:id', asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) return res.status(404).json({ error: 'Not found' });
  res.json(user);
}));
```

2. Wrap each async handler with try/catch manually:

```javascript
app.post('/api/orders', async (req, res, next) => {
  try {
    const order = await createOrder(req.body);
    res.status(201).json(order);
  } catch (err) {
    next(err);
  }
});
```

3. Upgrade to Express 5 which handles async errors natively:

```bash
npm install express@5
```

```javascript
// Express 5 automatically catches async errors
app.get('/api/items', async (req, res) => {
  const items = await Item.findAll(); // Thrown errors go to error handler
  res.json(items);
});
```

## Examples

```javascript
// Unhandled async error crashes the server
app.get('/api/reports', async (req, res) => {
  const report = await generateReport(); // If this throws, server crashes
  res.json(report);
});

// Fixed with asyncHandler
app.get('/api/reports', asyncHandler(async (req, res) => {
  const report = await generateReport();
  res.json(report);
}));
```

```text
UnhandledPromiseRejectionWarning: Error: Connection refused
```
