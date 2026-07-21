---
title: "[Solution] Express Next Function Called Twice Error"
description: "Fix Express errors where the next() function is called multiple times, causing double response headers."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A next() called twice error in Express occurs when `next()` is invoked more than once in a single request cycle, leading to "headers already sent" errors or double execution of downstream middleware.

## Common Causes

- `next()` called both in success and catch blocks
- Conditional logic missing `return` after `next()` call
- Race condition between async operations both calling `next()`
- Error handler calls `next(err)` but response is already sent
- Middleware does not short-circuit after sending a response

## How to Fix

1. Return after calling `next()` to prevent fallthrough:

```javascript
app.use(async (req, res, next) => {
  try {
    const user = await findUser(req.headers.authorization);
    if (!user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    req.user = user;
    return next(); // Return prevents further execution
  } catch (err) {
    return next(err);
  }
});
```

2. Use a flag to prevent double calls:

```javascript
app.use((req, res, next) => {
  let called = false;

  const done = (err) => {
    if (!called) {
      called = true;
      next(err);
    }
  };

  asyncOperation(done);
  timeoutHandler(done);
});
```

3. Restructure conditional middleware to avoid double calls:

```javascript
// Bug: next() called in both branches
app.use((req, res, next) => {
  if (req.query.token) {
    validateToken(req.query.token);
    next();
  }
  if (req.headers.authorization) {
    validateAuth(req.headers.authorization);
    next(); // Called twice if both conditions are true
  }
});

// Fixed: use else-if
app.use((req, res, next) => {
  if (req.query.token) {
    return validateToken(req.query.token, next);
  }
  if (req.headers.authorization) {
    return validateAuth(req.headers.authorization, next);
  }
  next();
});
```

## Examples

```javascript
// Bug: next() called after res.json()
app.get('/api/data', async (req, res, next) => {
  try {
    const data = await fetchData();
    res.json(data);
    next(); // Bug: response already sent
  } catch (err) {
    next(err);
  }
});

// Fixed: return after res.json()
app.get('/api/data', async (req, res, next) => {
  try {
    const data = await fetchData();
    return res.json(data);
  } catch (err) {
    return next(err);
  }
});
```

```text
Error [ERR_HTTP_HEADERS_SENT]: Cannot set headers after they are sent to the client
```
