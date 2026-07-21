---
title: "[Solution] React Rewrites Error"
description: "Rewrites not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Rewrites not working.

## Common Causes

Wrong config.

## How to Fix

Configure rewrites.

## Example

```javascript
module.exports = { async rewrites() { return [{ source: '/api/:path*', destination: 'https://api.example.com/:path*' }]; } };
```
