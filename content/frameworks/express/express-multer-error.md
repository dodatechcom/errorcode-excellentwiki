---
title: "[Solution] Express Multer Error"
description: "File upload failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

File upload failing.

## Common Causes

Not configured.

## How to Fix

Configure multer.

## Example

```javascript
const m = require('multer');
const u = m({ dest: 'uploads/' });
app.post('/upload', u.single('file'), (req, res) => res.json(req.file));
```
