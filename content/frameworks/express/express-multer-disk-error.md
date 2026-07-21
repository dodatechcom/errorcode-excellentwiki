---
title: "[Solution] Express Multer Disk Error"
description: "Multer disk storage failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Multer disk storage failing.

## Common Causes

Wrong config.

## How to Fix

Configure storage.

## Example

```javascript
const storage = multer.diskStorage({
  destination: 'uploads/',
  filename: (req, file, cb) => cb(null, file.originalname)
});
const u = multer({ storage });
```
