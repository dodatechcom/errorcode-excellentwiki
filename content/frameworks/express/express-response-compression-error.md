---
title: "[Solution] Express Response Compression Error"
description: "Fix Express response compression errors when the compression middleware fails to encode the response body."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
weight: 1
---

An Express response compression error occurs when the `compression` middleware fails to compress the response body, often resulting in corrupted output or a broken encoding stream.

## Common Causes

- Response body is too small to compress (overhead exceeds savings)
- Response is already compressed (double compression)
- `Content-Length` header does not match the compressed body
- Stream is not flushed before the connection closes
- `Content-Type` header missing, preventing compression detection

## How to Fix

1. Configure the compression threshold to skip small responses:

```javascript
const compression = require('compression');

app.use(compression({
  threshold: 1024, // Only compress responses > 1KB
  filter: (req, res) => {
    if (req.headers['x-no-compression']) return false;
    return compression.filter(req, res);
  }
}));
```

2. Prevent double compression when proxying:

```javascript
app.use(compression({
  filter: (req, res) => {
    if (res.getHeader('Content-Encoding')) return false;
    return compression.filter(req, res);
  }
}));
```

3. Ensure proper Content-Type for compression:

```javascript
app.use(compression({
  level: 6,
  memLevel: 8,
  flush: require('zlib').constants.Z_SYNC_FLUSH
}));
```

## Examples

```javascript
// Without threshold -- tiny responses waste CPU
app.use(compression());

// Fixed -- skip responses under 1KB
app.use(compression({ threshold: 1024 }));

app.get('/api/small', (req, res) => {
  res.json({ status: 'ok' }); // ~30 bytes, skipped by compression
});

app.get('/api/large', (req, res) => {
  res.json(generateLargePayload()); // Thousands of bytes, compressed
});
```

```text
Error: zlib error: incorrect header check
```
