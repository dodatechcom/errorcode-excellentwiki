---
title: "[Solution] Express Middleware Error Fix"
description: "Fix Express middleware errors. Handle async errors, error middleware signatures, and proper error propagation in Express.js."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["express", "middleware", "error-handler", "next", "expressjs"]
weight: 5
---

# Express Middleware Error

This error occurs when Express middleware throws an unhandled error or fails to properly pass errors to the error handler. Express requires specific error handling patterns.

## What This Error Means

Common error messages:

- `TypeError: Cannot read properties of undefined (reading 'status')`
- `UnhandledPromiseRejection`
- `Error: Route.get() requires a callback function`

Express middleware must call `next(err)` to forward errors. Async functions need explicit error handling.

## Common Causes

```javascript
// Cause 1: Async middleware without error handling
app.use('/api', async (req, res) => {
  const data = await fetchData(); // throws = unhandled
  res.json(data);
});

// Cause 2: Not calling next() on error
app.use((req, res, next) => {
  try {
    doSomething();
  } catch (err) {
    // forgot next(err)
  }
});

// Cause 3: Error handler missing (err, req, res, next) signature
app.use((err, req, res) => {
  res.status(500).send(err.message); // works but not standard
});

// Cause 4: Throwing in synchronous middleware
app.use('/api', (req, res) => {
  throw new Error('Something went wrong'); // crashes if no error handler
});
```

## How to Fix

### Fix 1: Add error-handling middleware

```javascript
// Must have 4 parameters
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message || 'Internal Server Error',
  });
});
```

### Fix 2: Use express-async-errors or wrapper

```javascript
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

app.get('/api/data', asyncHandler(async (req, res) => {
  const data = await fetchData();
  res.json(data);
}));
```

### Fix 3: Handle errors in Express 5

```javascript
// Express 5 handles async errors automatically
app.get('/api/data', async (req, res) => {
  const data = await fetchData(); // errors forwarded to error handler
  res.json(data);
});
```

### Fix 4: Use try-catch in async middleware

```javascript
app.get('/api/users', async (req, res, next) => {
  try {
    const users = await db.users.findMany();
    res.json(users);
  } catch (err) {
    next(err);
  }
});
```

## Examples

```javascript
// This triggers unhandled error
app.get('/api/data', async (req, res) => {
  const data = await fetch('http://api.example.com/data');
  // If fetch throws, no error handling
});

// Fix
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

app.get('/api/data', asyncHandler(async (req, res) => {
  const data = await fetch('http://api.example.com/data');
  res.json(data);
}));
```

## Related Errors

- [Express Route 404]({{< relref "/languages/javascript/express-route" >}}) — route not found
- [Express Params]({{< relref "/languages/javascript/express-params" >}}) — params undefined
- [Express Session]({{< relref "/languages/javascript/express-session" >}}) — session error
