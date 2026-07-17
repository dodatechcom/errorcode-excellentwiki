---
title: "Multer File Upload Error in Express"
description: "Fix Express Multer file upload errors when files are too large, invalid type, or upload configuration is misconfigured."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["multer", "upload", "file", "multipart", "express"]
weight: 5
---

## What This Error Means

Multer is the standard middleware for handling `multipart/form-data` in Express. Upload errors occur when files exceed size limits, have unexpected field names, or the form data is malformed. Without proper error handling, Multer throws uncaught exceptions that crash the request.

## Common Causes

- File exceeds the configured size limit (`limits.fileSize`)
- Field name in the form does not match the multer configuration
- Too many files uploaded in a single request
- Non-file fields sent as file uploads or vice versa
- Missing `enctype="multipart/form-data"` in HTML form

## How to Fix

### Configure Multer with Error Handling

```javascript
const multer = require('multer');

const upload = multer({
  storage: multer.diskStorage({
    destination: './uploads/',
    filename: (req, file, cb) => {
      cb(null, Date.now() + '-' + file.originalname);
    }
  }),
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB
  fileFilter: (req, file, cb) => {
    if (file.mimetype.startsWith('image/')) {
      cb(null, true);
    } else {
      cb(new Error('Only image files are allowed'), false);
    }
  }
});

app.post('/upload', upload.single('image'), (req, res) => {
  res.json({ filename: req.file.filename });
});

// Handle Multer errors
app.use((err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    if (err.code === 'LIMIT_FILE_SIZE') {
      return res.status(413).json({ error: 'File too large (max 5MB)' });
    }
    if (err.code === 'LIMIT_UNEXPECTED_FILE') {
      return res.status(400).json({ error: 'Unexpected field name' });
    }
    return res.status(400).json({ error: err.message });
  }
  next(err);
});
```

### Use Memory Storage for Small Files

```javascript
const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 1024 * 1024 } // 1MB
});

app.post('/avatar', upload.single('avatar'), (req, res) => {
  // req.file.buffer contains the file data
  processImage(req.file.buffer);
  res.json({ uploaded: true });
});
```

### Handle Multiple File Uploads

```javascript
const upload = multer({
  storage: multer.diskStorage({ /* ... */ }),
  limits: { fileSize: 10 * 1024 * 1024 }
});

app.post('/gallery', upload.array('photos', 10), (req, res) => {
  // req.files is an array of uploaded files
  res.json({ uploaded: req.files.length });
});
```

## Related Errors

- [Express BodyParser Error]({{< relref "/frameworks/express/express-body-parser-error-v2" >}}) — JSON parse failure
- [Express Validation Error]({{< relref "/frameworks/express/express-validation-error-v2" >}}) — input validation failure
