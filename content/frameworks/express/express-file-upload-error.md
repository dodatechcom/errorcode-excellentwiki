---
title: "[Solution] Express File Upload Error"
description: "Fix Express file upload errors. Resolve Multer and file upload issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file-upload", "multer", "multipart", "upload", "express"]
weight: 5
---

An Express file upload error occurs when file uploads fail due to configuration issues, size limits, or missing middleware.

## Common Causes

- Multer middleware not configured
- File size exceeds limit
- File type not allowed
- Missing multipart/form-data Content-Type
- Upload directory does not exist

## How to Fix

### Configure Multer

```javascript
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('file'), (req, res) => {
  console.log(req.file);
  res.json({ file: req.file });
});
```

### Set File Size Limit

```javascript
const upload = multer({
  dest: 'uploads/',
  limits: { fileSize: 5 * 1024 * 1024 } // 5MB
});
```

### Filter File Types

```javascript
const upload = multer({
  dest: 'uploads/',
  fileFilter: (req, file, cb) => {
    if (file.mimetype === 'image/jpeg' || file.mimetype === 'image/png') {
      cb(null, true);
    } else {
      cb(new Error('Only JPEG and PNG allowed'), false);
    }
  }
});
```

### Handle Multer Errors

```javascript
app.use((err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    if (err.code === 'LIMIT_FILE_SIZE') {
      return res.status(413).json({ error: 'File too large' });
    }
  }
  next(err);
});
```

## Examples

```javascript
// Example 1: File too large
// MulterError: File too large
// Fix: increase limits.fileSize

// Example 2: Missing multipart header
// Fix: ensure client sends multipart/form-data
```

## Related Errors

- [Express BodyParser Error]({{< relref "/frameworks/express/express-body-parser-error" >}}) — body parsing error
- [Express Validation Error]({{< relref "/frameworks/express/express-validation-error" >}}) — validation error
