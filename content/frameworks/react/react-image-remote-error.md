---
title: "[Solution] React Image Remote Error"
description: "Remote image not loading."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Remote image not loading.

## Common Causes

Domain not allowed.

## How to Fix

Add to config.

## Example

```javascript
// next.config.js
module.exports = { images: { remotePatterns: [{ hostname: 'example.com' }] } };
```
