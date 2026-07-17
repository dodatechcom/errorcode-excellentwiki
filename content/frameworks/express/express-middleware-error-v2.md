---
title: "Express Middleware: Missing next() Call"
description: "Fix Express middleware errors caused by missing next() calls that hang requests and block the middleware chain."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

When an Express middleware function does not call `next()` and does not send a response, the request hangs indefinitely. The client never receives a response, and subsequent middleware or route handlers are never executed. This is one of the most common and frustrating issues in Express applications.

## Common Causes

- Middleware performs an operation but forgets to call `next()` at the end
- Conditional logic in middleware has a code path that skips `next()`
- Async middleware does not `await` the promise before calling `next()`
- Error thrown inside middleware without calling `next(err)`
- Middleware intended as a terminal handler is placed in the middle of a chain

## How to Fix

### Always Call next() or Send a Response

```javascript
app.use((req, res, next) => {
  console.log('Request received:', req.method, req.url);
  next(); // Must call next() to pass control forward
});
```

### Handle Async Middleware Properly

```javascript
app.use(async (req, res, next) => {
  try {
    const user = await fetchUser(req.headers.authorization);
    req.user = user;
    next(); // Call next after async work completes
  } catch (err) {
    next(err); // Forward error to error-handling middleware
  }
});
```

### Add a Timeout Safety Net

```javascript
app.use((req, res, next) => {
  const timeout = setTimeout(() => {
    if (!res.headersSent) {
      next(new Error('Middleware timeout'));
    }
  }, 5000);

  res.on('finish', () => clearTimeout(timeout));
  next();
});
```

### Use express-async-errors for Automatic Handling

```javascript
require('express-async-errors');

app.get('/data', async (req, res) => {
  const data = await fetchData(); // Errors auto-forwarded to next(err)
  res.json(data);
});
```

## Related Errors

- [Express 404 Route Not Found]({{< relref "/frameworks/express/express-404-error-v2" >}}) — route not found
- [Express BodyParser Error]({{< relref "/frameworks/express/express-body-parser-error-v2" >}}) — body parsing failure
