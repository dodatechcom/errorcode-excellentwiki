---
title: "[Solution] React Redirects Error"
description: "Redirects not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Redirects not working.

## Common Causes

Wrong config.

## How to Fix

Configure redirects.

## Example

```javascript
module.exports = { async redirects() { return [{ source: '/old', destination: '/new', permanent: true }]; } };
```
