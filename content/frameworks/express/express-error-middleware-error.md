---
title: "[Solution] Express Error Middleware Error"
description: "Error not caught."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Error not caught.

## Common Causes

Wrong signature.

## How to Fix

Need 4 params.

## Example

```javascript
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});
```
