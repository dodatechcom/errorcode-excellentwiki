---
title: "[Solution] React Next.js Config Images Error"
description: "Image config wrong."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Image config wrong.

## Common Causes

Wrong format.

## How to Fix

Use remotePatterns.

## Example

```javascript
module.exports = { images: { remotePatterns: [{ protocol: 'https', hostname: '**.example.com' }] } };
```
