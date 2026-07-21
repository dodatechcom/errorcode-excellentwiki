---
title: "[Solution] Express Content-Type Mismatch Error"
description: "Fix Express content-type mismatch errors when the request Content-Type header does not match the parser configuration."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A content-type mismatch error in Express occurs when the request's `Content-Type` header does not match the configured body parser, causing the body to remain `undefined` or throw a parsing error.

## Common Causes

- Client sends `text/plain` but server only has `express.json()` configured
- `Content-Type` header includes charset or boundary parameters
- Multipart form data sent without `multer` middleware
- `express.urlencoded()` not configured for HTML form submissions
- Client sets incorrect Content-Type in fetch or axios requests

## How to Fix

1. Configure body parsers for all expected content types:

```javascript
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.text());
app.use(express.raw({ type: 'application/octet-stream' }));
```

2. Use route-specific middleware for different content types:

```javascript
app.post('/api/json', express.json(), (req, res) => {
  res.json({ type: 'json', body: req.body });
});

app.post('/api/form', express.urlencoded({ extended: true }), (req, res) => {
  res.json({ type: 'form', body: req.body });
});

app.post('/api/webhook', express.raw({ type: '*/*' }), (req, res) => {
  res.json({ type: 'raw', length: req.body.length });
});
```

3. Handle multipart form data with multer:

```javascript
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

app.post('/api/upload', upload.single('file'), (req, res) => {
  res.json({
    file: req.file,
    fields: req.body
  });
});
```

## Examples

```javascript
// Client sends form data but server expects JSON
fetch('/api/data', {
  method: 'POST',
  headers: { 'Content-Type': 'text/plain' },
  body: 'some text'
});

// Server only has express.json() -- body is undefined
app.use(express.json());
app.post('/api/data', (req, res) => {
  console.log(req.body); // undefined
});

// Fixed: add text parser
app.use(express.text());
```

```text
SyntaxError: Unexpected token s in JSON at position 0
```
