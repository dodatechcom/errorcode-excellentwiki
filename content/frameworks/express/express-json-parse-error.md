---
title: "[Solution] Express JSON Parse Error"
description: "JSON.parse failing on request body."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

JSON.parse failing on request body.

## Common Causes

Wrong content type.

## How to Fix

Use express.json() middleware.

## Example

```javascript
app.use(express.json());
app.post('/api', (req, res) => {
  const data = req.body; // already parsed
});
```
