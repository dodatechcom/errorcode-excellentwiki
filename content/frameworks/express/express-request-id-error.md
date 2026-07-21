---
title: "[Solution] Express Request ID Error"
description: "Fix Express request ID errors when unique identifiers are missing from logs or responses for debugging."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A request ID error in Express occurs when unique identifiers are not generated or propagated across requests, making it impossible to trace requests through multiple services or correlate log entries.

## Common Causes

- No request ID middleware configured
- Downstream services do not forward the request ID
- Request ID not included in error responses
- Different services generate independent IDs instead of sharing one
- Logging middleware does not include the request ID

## How to Fix

1. Generate unique request IDs with the `uuid` package:

```javascript
const { v4: uuidv4 } = require('uuid');

app.use((req, res, next) => {
  req.id = req.headers['x-request-id'] || uuidv4();
  res.set('X-Request-Id', req.id);
  next();
});
```

2. Include request ID in all log entries:

```javascript
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    console.log(JSON.stringify({
      requestId: req.id,
      method: req.method,
      url: req.url,
      status: res.statusCode,
      duration: Date.now() - start
    }));
  });
  next();
});
```

3. Forward request ID to downstream services:

```javascript
async function fetchFromAPI(url) {
  const response = await fetch(url, {
    headers: {
      'X-Request-Id': req.id // Forward the same ID
    }
  });
  return response.json();
}
```

## Examples

```javascript
// Bug: no request ID -- impossible to trace
app.get('/api/order/:id', async (req, res) => {
  console.log(`Processing order ${req.params.id}`);
  // Which request produced this log?
});

// Fixed: request ID in every log
const { v4: uuidv4 } = require('uuid');

app.use((req, res, next) => {
  req.id = req.headers['x-request-id'] || uuidv4();
  res.set('X-Request-Id', req.id);
  next();
});

app.get('/api/order/:id', async (req, res) => {
  console.log(`[${req.id}] Processing order ${req.params.id}`);
  // Now traceable: abc-123-def processing order 42
});
```

```text
Missing X-Request-Id header in downstream service call
```
