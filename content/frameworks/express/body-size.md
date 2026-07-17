---
title: "Payload Too Large (413)"
description: "Express rejects a request because the body exceeds the configured size limit"
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the request body is larger than the limit set in `body-parser` or Express's built-in JSON middleware. Express returns HTTP 413 Payload Too Large.

## Common Causes

- File upload exceeds the default body size limit (100KB for `urlencoded`)
- JSON body limit set too low for the use case
- Client sending large payloads without proper chunking
- Missing `limit` configuration in middleware

## How to Fix

1. Set appropriate body size limits:

```javascript
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));
```

2. Configure file upload limits for `multer`:

```javascript
const multer = require('multer');
const upload = multer({
  storage: multer.diskStorage({ destination: './uploads/' }),
  limits: { fileSize: 50 * 1024 * 1024 } // 50MB
});

app.post('/upload', upload.single('file'), (req, res) => {
  res.json({ filename: req.file.filename });
});
```

3. Handle the 413 error explicitly:

```javascript
app.use((err, req, res, next) => {
  if (err.type === 'entity.too.large') {
    return res.status(413).json({ error: 'Payload too large' });
  }
  next(err);
});
```

## Examples

```javascript
// Client uploading a large file without setting limits
fetch('/upload', {
  method: 'POST',
  body: largeFileBlob
})
// 413 Payload Too Large
```

```text
PayloadTooLargeError: request entity too large
    at readStream (node_modules/raw-body/index.js:103)
```

## Related Errors

- [JSON parse error]({{< relref "/frameworks/express/json-parse" >}})
