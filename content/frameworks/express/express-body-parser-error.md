---
title: "[Solution] Express BodyParser Error — body parsing error"
description: "Fix Express BodyParser errors. Resolve request body parsing failures."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["body-parser", "json", "parse", "request", "express"]
weight: 5
---

An Express BodyParser error occurs when Express cannot parse the request body. This commonly happens with JSON, URL-encoded, or multipart data.

## Common Causes

- Missing body parser middleware
- Invalid JSON in request body
- Content-Type header does not match parser
- Request body too large
- Parsing middleware registered after routes

## How to Fix

### Register Body Parser

```javascript
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
```

### Configure Size Limit

```javascript
app.use(express.json({ limit: '10mb' }));
```

### Handle Parse Errors

```javascript
app.use(express.json());
app.use((err, req, res, next) => {
  if (err.type === 'entity.parse.failed') {
    return res.status(400).json({ error: 'Invalid JSON' });
  }
  next(err);
});
```

### Use Multer for File Uploads

```javascript
const multer = require('multer');
app.post('/upload', multer().single('file'), (req, res) => {
  console.log(req.file);
});
```

### Check Content-Type Header

```javascript
// Client must send:
// Content-Type: application/json
fetch('/api', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
});
```

## Examples

```javascript
// Example 1: Missing body parser
app.post('/api', (req, res) => {
  console.log(req.body); // undefined
});
// Fix: add app.use(express.json()) before routes

// Example 2: Invalid JSON
// POST /api with body: {invalid json}
// Fix: send valid JSON or handle parse error
```

## Related Errors

- [Express Validation Error]({{< relref "/frameworks/express/express-validation-error" >}}) — validation error
- [Express File Upload Error]({{< relref "/frameworks/express/express-file-upload-error" >}}) — file upload error
