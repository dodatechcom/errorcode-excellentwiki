---
title: "[Solution] Express Middleware Error — middleware error"
description: "Fix Express middleware errors. Resolve middleware execution failures."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["middleware", "error", "next", "handler", "express"]
weight: 5
---

An Express middleware error occurs when middleware fails to pass control to the next handler or throws an unhandled exception. This can crash the request or the entire server.

## Common Causes

- Middleware does not call `next()` or `res.send()`
- Asynchronous middleware missing `async/await` or `.catch()`
- Error thrown but not caught
- Middleware order is incorrect
- Middleware modifies headers after response sent

## How to Fix

### Ensure next() or Response

```javascript
app.use((req, res, next) => {
  // Do something
  next(); // Must call next() or send response
});
```

### Handle Async Errors

```javascript
app.use(async (req, res, next) => {
  try {
    const result = await someAsyncOperation();
    next();
  } catch (err) {
    next(err); // Pass error to error handler
  }
});
```

### Use Error-Handling Middleware

```javascript
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong' });
});
```

### Check Middleware Order

```javascript
// Wrong order - 404 handler catches everything
app.use(express.json()); // Must come before routes
app.use('/api', apiRouter);
```

## Examples

```javascript
// Example 1: Missing next()
app.use((req, res, next) => {
  console.log(req.url);
  // Missing next() - request hangs
  next();
});

// Example 2: Async error
app.get('/data', async (req, res) => {
  const data = await fetchData(); // If this throws, server crashes
  res.json(data);
});
// Fix: wrap in try-catch or use express-async-errors
```

## Related Errors

- [Express 404 Error]({{< relref "/frameworks/express/express-404-error" >}}) — route not found
- [Express BodyParser Error]({{< relref "/frameworks/express/express-body-parser-error" >}}) — body parsing error
