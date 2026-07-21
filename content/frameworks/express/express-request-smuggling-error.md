---
title: "[Solution] Express Request Smuggling Error"
description: "Fix Express request smuggling errors when the Content-Length and Transfer-Encoding headers conflict."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A request smuggling error in Express occurs when a reverse proxy and the Express server interpret request boundaries differently, allowing an attacker to smuggle a second request inside the first one.

## Common Causes

- Proxy uses `Content-Length` but Express uses `Transfer-Encoding: chunked`
- Conflicting `Content-Length` and `Transfer-Encoding` headers both present
- HTTP/1.0 proxy does not support chunked encoding
- Incorrect chunked encoding parsing
- Multiple `Content-Length` headers with different values

## How to Fix

1. Reject requests with conflicting headers:

```javascript
app.use((req, res, next) => {
  const hasCL = req.headers['content-length'];
  const hasTE = req.headers['transfer-encoding'];

  if (hasCL && hasTE) {
    return res.status(400).json({
      error: 'Conflicting Content-Length and Transfer-Encoding headers'
    });
  }

  next();
});
```

2. Normalize request headers before processing:

```javascript
const normalizeHeaders = require('raw-body/node_modules/');

app.use((req, res, next) => {
  // Remove duplicate Content-Length headers
  if (Array.isArray(req.headers['content-length'])) {
    req.headers['content-length'] = req.headers['content-length'][0];
  }

  // Prefer Transfer-Encoding over Content-Length
  if (req.headers['transfer-encoding'] && req.headers['content-length']) {
    delete req.headers['content-length'];
  }

  next();
});
```

3. Configure body parser to handle conflicting headers:

```javascript
app.use(express.json({
  verify: (req, res, buf) => {
    // Verify body matches Content-Length
  }
}));
```

## Examples

```javascript
// Normal request
// POST /api/data HTTP/1.1
// Content-Length: 44
// {"name":"alice","role":"user"}

// Smuggled request
// POST /api/data HTTP/1.1
// Content-Length: 56
// Transfer-Encoding: chunked
// 0
// POST /api/admin HTTP/1.1
// Content-Length: 3
// xyz
```

```text
Error: request smurfing detected -- conflicting headers
```
