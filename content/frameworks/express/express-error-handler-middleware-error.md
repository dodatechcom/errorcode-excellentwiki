---
title: "[Solution] Express Error Handler Middleware Error"
description: "Fix Express error handler middleware that does not catch thrown errors or returns incorrect status codes."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An Express error handler middleware error occurs when the custom error handler does not properly catch and process errors passed via `next(err)`, or when the error handler itself throws an exception.

## Common Causes

- Error handler middleware missing the 4-parameter signature `(err, req, res, next)`
- Error handler registered before route definitions
- Error handler calls `next()` without sending a response
- Error handler does not handle all error types
- Error handler sets headers after the response is already sent

## How to Fix

1. Define a proper error handler with all four parameters:

```javascript
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: {
      message: err.message || 'Internal Server Error',
      ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
    }
  });
});
```

2. Register error handler after all routes and middleware:

```javascript
// Routes first
app.use('/api', apiRouter);
app.use('/admin', adminRouter);

// Error handler last
app.use(errorHandler);
```

3. Create typed error classes for specific status codes:

```javascript
class AppError extends Error {
  constructor(message, status) {
    super(message);
    this.status = status;
  }
}

app.get('/api/users/:id', async (req, res, next) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) throw new AppError('User not found', 404);
    res.json(user);
  } catch (err) {
    next(err);
  }
});

app.use((err, req, res, next) => {
  const status = err.status || 500;
  res.status(status).json({ error: err.message });
});
```

## Examples

```javascript
// Bug: only 3 parameters -- Express ignores this as error handler
app.use((err, req, res) => {
  res.status(500).json({ error: err.message });
});

// Correct: 4 parameters required
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});
```

```text
Error [ERR_HTTP_HEADERS_SENT]: Cannot set headers after they are sent to the client
```
