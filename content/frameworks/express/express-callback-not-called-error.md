---
title: "[Solution] Express Callback Not Called Error"
description: "Fix Express errors where the callback function is never invoked, leaving requests hanging indefinitely."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when an Express middleware or route handler never calls the `next()` function or sends a response, causing the request to hang. The client eventually times out waiting for a response.

## Common Causes

- Async middleware forgets to call `next()` on success
- Conditional branches in middleware miss the `next()` call
- Error in middleware prevents `next()` from executing
- Route handler has a code path that returns without calling `res.send()`
- `next()` is called multiple times causing unpredictable behavior

## How to Fix

1. Ensure every code path in middleware calls `next()` or sends a response:

```javascript
app.use(async (req, res, next) => {
  try {
    const user = await findUser(req.headers.authorization);
    if (!user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }
    req.user = user;
    next();
  } catch (err) {
    next(err);
  }
});
```

2. Use a wrapper function to catch forgotten `next()` calls:

```javascript
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/data', asyncHandler(async (req, res) => {
  const data = await fetchData();
  res.json(data);
}));
```

3. Debug hanging requests with a timeout logger:

```javascript
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    if (duration > 5000) {
      console.warn(`Slow request: ${req.method} ${req.url} took ${duration}ms`);
    }
  });
  next();
});
```

## Examples

```javascript
// Bug: next() not called when user is found
app.use((req, res, next) => {
  const user = findUser(req.query.id);
  if (!user) {
    return res.status(404).json({ error: 'Not found' });
  }
  // Missing: next() -- request hangs forever
});

// Fixed
app.use((req, res, next) => {
  const user = findUser(req.query.id);
  if (!user) {
    return res.status(404).json({ error: 'Not found' });
  }
  req.user = user;
  next();
});
```

```text
Request hangs and client receives: ERR_CONNECTION_TIMED_OUT
```
