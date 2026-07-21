---
title: "[Solution] Express Request Body Too Large Error"
description: "Fix Express request body too large errors when incoming payloads exceed the configured size limit."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A request body too large error in Express occurs when an incoming request exceeds the body parser's size limit, triggering a `PayloadTooLargeError` or `413` status code.

## Common Causes

- Default body size limit of 100KB exceeded
- File uploads sent through JSON body parser instead of multer
- Large JSON payloads not anticipated in the API design
- Multipart boundary parsing fails before size check
- Client sends chunked encoding with accumulated size over limit

## How to Fix

1. Increase the body size limit for specific routes:

```javascript
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));
```

2. Set different limits per route:

```javascript
app.post('/api/small', express.json({ limit: '100kb' }), (req, res) => {
  res.json({ received: req.body });
});

app.post('/api/upload', express.json({ limit: '50mb' }), (req, res) => {
  res.json({ received: req.body });
});
```

3. Handle the error gracefully:

```javascript
app.use(express.json({ limit: '5mb' }));

app.use((err, req, res, next) => {
  if (err.type === 'entity.too.large') {
    return res.status(413).json({
      error: 'Request body too large',
      maxSize: '5MB'
    });
  }
  next(err);
});
```

## Examples

```javascript
// Bug: default 100KB limit too small
app.use(express.json()); // Default limit: 100kb

app.post('/api/import', (req, res) => {
  // Fails with large data imports
  importData(req.body);
});

// Fixed: increase limit
app.use(express.json({ limit: '50mb' }));

app.post('/api/import', (req, res) => {
  importData(req.body);
});
```

```text
PayloadTooLargeError: request entity too large
```
