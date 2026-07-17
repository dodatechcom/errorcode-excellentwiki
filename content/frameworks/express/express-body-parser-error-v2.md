---
title: "Express BodyParser JSON Parse Error"
description: "Fix Express BodyParser errors when incoming request bodies contain invalid JSON or exceed size limits."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

When Express receives a request with a `Content-Type: application/json` header but the body contains malformed JSON, the BodyParser middleware throws a `SyntaxError`. Without a custom error handler, this results in an unhelpful 400 error or an uncaught exception that can crash the process.

## Common Causes

- Client sends invalid JSON (missing commas, unclosed brackets, trailing commas)
- Request body exceeds the default size limit (100kb)
- Non-JSON content sent with `application/json` content type
- Double-parsing: middleware already parsed the body before your route runs
- Request body is empty or `null` when JSON is expected

## How to Fix

### Configure BodyParser with Error Handling

```javascript
app.use(express.json({ limit: '10mb' }));

// Custom error handler for body-parser failures
app.use((err, req, res, next) => {
  if (err.type === 'entity.parse.failed') {
    return res.status(400).json({
      error: 'Invalid JSON',
      message: 'The request body contains malformed JSON'
    });
  }
  next(err);
});
```

### Validate JSON Before Processing

```javascript
app.post('/data', (req, res) => {
  if (!req.body || Object.keys(req.body).length === 0) {
    return res.status(400).json({ error: 'Request body is empty' });
  }
  // Process valid JSON body
  res.json({ received: req.body });
});
```

### Handle Content-Type Mismatch

```javascript
app.use(express.json({
  type: ['application/json', 'application/vnd.api+json']
}));

app.use((err, req, res, next) => {
  if (err.type === 'parse') {
    return res.status(400).json({ error: 'Invalid JSON in request body' });
  }
  next(err);
});
```

### Test with curl

```bash
# Valid JSON
curl -X POST http://localhost:3000/api/data \
  -H "Content-Type: application/json" \
  -d '{"name": "test", "value": 42}'

# Invalid JSON (missing closing bracket)
curl -X POST http://localhost:3000/api/data \
  -H "Content-Type: application/json" \
  -d '{"name": "test"'
```

## Related Errors

- [Express Validation Error]({{< relref "/frameworks/express/express-validation-error-v2" >}}) — input validation failure
- [Express 404 Route Not Found]({{< relref "/frameworks/express/express-404-error-v2" >}}) — undefined route
