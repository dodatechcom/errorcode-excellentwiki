---
title: "[Solution] Express req.baseUrl Error"
description: "req.baseUrl not working."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

req.baseUrl not working.

## Common Causes

Not mounted.

## How to Fix

Mount sub-app.

## Example

```javascript
const api = express.Router();
app.use('/api', api);
// In api: req.baseUrl = '/api'
```
