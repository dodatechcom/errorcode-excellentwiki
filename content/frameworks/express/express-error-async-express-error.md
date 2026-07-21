---
title: "[Solution] Express Error Async Express Error"
description: "Async errors not caught."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Async errors not caught.

## Common Causes

No handler.

## How to Fix

Use try/catch.

## Example

```javascript
require('express-async-errors');
app.get('/api', async (req, res) => {
  const d = await getData();
  res.json(d);
});
```
