---
title: "[Solution] Express Rate Limiting Error"
description: "All requests blocked."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

All requests blocked.

## Common Causes

Limit too low.

## How to Fix

Adjust rate.

## Example

```javascript
const rl = require('express-rate-limit');
app.use(rl({ windowMs: 15*60*1000, max: 100 }));
```
