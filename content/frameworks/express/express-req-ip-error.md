---
title: "[Solution] Express req.ip Error"
description: "Wrong IP address."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Wrong IP address.

## Common Causes

Proxy not trusted.

## How to Fix

Set trust proxy.

## Example

```javascript
app.set('trust proxy', true);
const ip = req.ip;
```
