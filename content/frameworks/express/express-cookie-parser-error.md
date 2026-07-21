---
title: "[Solution] Express Cookie Parser Error"
description: "Cookies not parsed."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Cookies not parsed.

## Common Causes

Not used.

## How to Fix

Add middleware.

## Example

```javascript
const cp = require('cookie-parser');
app.use(cp());
```
