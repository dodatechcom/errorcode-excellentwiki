---
title: "SyntaxError: Unexpected token in JSON"
description: "Express fails to parse request body because it contains invalid JSON"
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Express (via `body-parser`) receives a request with a `Content-Type: application/json` header but the body contains malformed JSON.

## Common Causes

- Malformed JSON in the request body (missing commas, extra quotes)
- Request body is empty or raw text when JSON was expected
- `body-parser` middleware not configured
- Using wrong `Content-Type` header in the client

## How to Fix

1. Add body-parser middleware with error handling:

```javascript
const express = require('express');
const app = express();

app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Global JSON error handler
app.use((err, req, res, next) => {
  if (err.type === 'entity.parse.failed') {
    return res.status(400).json({ error: 'Invalid JSON' });
  }
  next(err);
});
```

2. Validate JSON on the client before sending:

```javascript
// Client-side validation
const data = { name: "Alice" };
const json = JSON.stringify(data);
fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: json
});
```

3. Set a body size limit to reject oversized payloads:

```javascript
app.use(express.json({ limit: '1mb' }));
```

## Examples

```javascript
// Sending malformed JSON
fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: '{"name": "Alice", "age": }'  // missing value
})
```

```text
SyntaxError: Unexpected token } in JSON at position 23
at JSON.parse (<anonymous>)
```

## Related Errors

- [Payload too large]({{< relref "/frameworks/express/body-size" >}})
