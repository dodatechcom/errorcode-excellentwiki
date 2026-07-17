---
title: "Compression Middleware Error in Express"
description: "Fix Express compression middleware errors when response encoding fails or compressed output is corrupted."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `compression` middleware compresses response bodies using gzip or deflate. Errors occur when the response stream is already closed, headers are sent prematurely, or the encoding algorithm encounters invalid data. These errors can cause corrupted responses or unhandled stream exceptions.

## Common Causes

- Response headers already sent before compression starts
- `Content-Length` header is set manually, conflicting with compression
- Response body is already compressed (double-compression)
- Stream piping fails due to a broken client connection
- Compression level is set too high, causing memory issues

## How to Fix

### Install and Configure Compression

```javascript
const compression = require('compression');

app.use(compression({
  level: 6, // Balanced speed/compression
  threshold: 1024, // Only compress responses > 1KB
  filter: (req, res) => {
    if (req.headers['x-no-compression']) {
      return false; // Skip compression for this request
    }
    return compression.filter(req, res);
  }
}));
```

### Handle Compression Errors Gracefully

```javascript
const compression = require('compression');

app.use(compression());

app.use((err, req, res, next) => {
  if (err.code === 'ERR_STREAM_PREMATURE_CLOSE') {
    console.warn('Client disconnected before compression completed');
    return; // Don't send error — client is gone
  }
  next(err);
});
```

### Avoid Double Compression

```javascript
// Wrong: compression before a response-already-compressed route
app.use(compression());
app.use('/static', express.static('public')); // Files already compressed

// Correct: skip compression for static files
app.use(compression({
  filter: (req, res) => {
    if (req.path.match(/\.(gz|br|zip)$/)) {
      return false; // Already compressed
    }
    return compression.filter(req, res);
  }
}));
```

### Set Correct Headers After Compression

```javascript
app.use(compression());

app.get('/data', (req, res) => {
  // Don't set Content-Length manually — compression handles it
  res.set('Content-Type', 'application/json');
  res.json(largeObject);
});
```

## Related Errors

- [Express SSL Error]({{< relref "/frameworks/express/express-ssl-error-v2" >}}) — HTTPS certificate issues
- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error-v2" >}}) — middleware chain issues
