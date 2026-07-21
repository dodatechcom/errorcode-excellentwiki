---
title: "[Solution] Express Response Not Sent"
description: "Request hanging."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Request hanging.

## Common Causes

res.send not called.

## How to Fix

Always send.

## Example

```javascript
app.get('/api', (req, res) => { res.json({ ok: true }); });
```
