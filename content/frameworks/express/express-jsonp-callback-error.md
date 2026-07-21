---
title: "[Solution] Express JSONP Callback Error"
description: "JSONP not working."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

JSONP not working.

## Common Causes

No callback.

## How to Fix

Use jsonp.

## Example

```javascript
app.get('/api', (req, res) => { res.jsonp({ d: 'ok' }); });
```
