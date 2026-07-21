---
title: "[Solution] Express Trust Proxy Error"
description: "Wrong IP behind proxy."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Wrong IP behind proxy.

## Common Causes

Not set.

## How to Fix

Set trust proxy.

## Example

```javascript
app.set('trust proxy', 1);
```
