---
title: "[Solution] Express Helmet Middleware Error"
description: "Helmet too restrictive."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Helmet too restrictive.

## Common Causes

Default settings.

## How to Fix

Configure options.

## Example

```javascript
const h = require('helmet');
app.use(h({ contentSecurityPolicy: false }));
```
