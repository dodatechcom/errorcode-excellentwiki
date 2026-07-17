---
title: "[Solution] Express Compression Error"
description: "Fix Express compression errors. Resolve gzip/deflate compression issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Express compression error occurs when response compression fails or is misconfigured. This can cause encoding errors or broken responses.

## Common Causes

- Compression middleware not configured
- Incompatible encoding with response content
- Double compression applied
- Streaming response compression issues
- Memory issues with large uncompressed responses

## How to Fix

### Add Compression Middleware

```javascript
const compression = require('compression');

app.use(compression());
```

### Configure Compression Options

```javascript
app.use(compression({
  level: 6, // Compression level (1-9)
  threshold: 1024, // Only compress responses > 1KB
  filter: (req, res) => {
    if (req.headers['x-no-compression']) return false;
    return compression.filter(req, res);
  }
}));
```

### Exclude Specific Routes

```javascript
app.get('/image', (req, res, next) => {
  res.setHeader('Content-Encoding', 'identity');
  next();
});
```

### Check Content-Encoding Header

```javascript
app.use((req, res, next) => {
  res.on('finish', () => {
    console.log('Content-Encoding:', res.getHeader('Content-Encoding'));
  });
  next();
});
```

## Examples

```javascript
// Example 1: No compression
// Response: 100KB uncompressed
// Fix: add compression middleware

// Example 2: Double compression
// Content-Encoding: gzip, gzip
// Fix: check middleware order, add only once
```

## Related Errors

- [Express SSL Error]({{< relref "/frameworks/express/express-ssl-error" >}}) — SSL/TLS error
- [Express Static Error]({{< relref "/frameworks/express/express-static-error" >}}) — static file serving error
