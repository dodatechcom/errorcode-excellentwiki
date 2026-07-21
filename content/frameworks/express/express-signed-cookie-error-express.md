---
title: "[Solution] Express Signed Cookie Error Express"
description: "Signed cookies not working."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Signed cookies not working.

## Common Causes

No secret.

## How to Fix

Provide secret.

## Example

```javascript
app.use(cookieParser('secret'));
```
