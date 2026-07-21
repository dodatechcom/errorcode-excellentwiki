---
title: "[Solution] Express Async Error Unhandled"
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
app.get('/api', async (req, res) => {
  try { res.json(await getData()); }
  catch(e) { next(e); }
});
```
