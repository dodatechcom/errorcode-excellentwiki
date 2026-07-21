---
title: "[Solution] Express CORS Middleware Error"
description: "CORS blocking."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

CORS blocking.

## Common Causes

Not configured.

## How to Fix

Add cors.

## Example

```javascript
const cors = require('cors');
app.use(cors({ origin: 'http://localhost:3000' }));
```
