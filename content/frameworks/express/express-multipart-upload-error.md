---
title: "[Solution] Express Multipart Upload Error"
description: "Fix Express multipart upload errors when file uploads fail with malformed request or missing file data."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A multipart upload error in Express occurs when `multer` or another multipart parser fails to process file uploads due to incorrect configuration, missing field names, or oversized files.

## Common Causes

- `multer` not configured with correct `dest` or storage
- Field name in the form does not match the `upload.single()` parameter
- No file uploaded when the route expects one
- File exceeds the configured size limit
- Missing `enctype="multipart/form-data"` on the HTML form

## How to Fix

1. Configure multer with storage and limits:

```javascript
const multer = require('multer');

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, 'uploads/'),
  filename: (req, file, cb) => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, uniqueSuffix + path.extname(file.originalname));
  }
});

const upload = multer({
  storage,
  limits: { fileSize: 10 * 1024 * 1024 }, // 10MB
  fileFilter: (req, file, cb) => {
    const allowed = /jpeg|jpg|png|pdf/;
    const ext = allowed.test(path.extname(file.originalname).toLowerCase());
    const mime = allowed.test(file.mimetype);
    cb(null, ext && mime);
  }
});
```

2. Handle multiple file fields:

```javascript
app.post('/api/profile', upload.fields([
  { name: 'avatar', maxCount: 1 },
  { name: 'documents', maxCount: 5 }
]), (req, res) => {
  const avatar = req.files['avatar'][0];
  const docs = req.files['documents'];
  res.json({ avatar: avatar.path, documents: docs.map(d => d.path) });
});
```

3. Handle multer errors gracefully:

```javascript
app.use((err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    if (err.code === 'LIMIT_FILE_SIZE') {
      return res.status(413).json({ error: 'File too large' });
    }
    if (err.code === 'LIMIT_UNEXPECTED_FILE') {
      return res.status(400).json({ error: 'Unexpected file field' });
    }
    return res.status(400).json({ error: err.message });
  }
  next(err);
});
```

## Examples

```javascript
// Bug: field name mismatch
// HTML: <input type="file" name="photo">
app.post('/upload', upload.single('avatar'), (req, res) => {
  console.log(req.file); // undefined -- field name does not match
});

// Fixed: match field names
app.post('/upload', upload.single('photo'), (req, res) => {
  console.log(req.file); // File object
});
```

```text
MulterError: Unexpected field
```
