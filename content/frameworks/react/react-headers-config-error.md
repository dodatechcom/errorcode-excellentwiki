---
title: "[Solution] React Headers Config Error"
description: "Headers not setting."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Headers not setting.

## Common Causes

Wrong config.

## How to Fix

Configure headers.

## Example

```javascript
module.exports = { async headers() { return [{ source: '/api/:path*', headers: [{ key: 'X-Custom', value: 'val' }] }]; } };
```
