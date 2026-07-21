---
title: "[Solution] Next.js Image Optimization Error"
description: "Image not optimizing."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Image not optimizing.

## Common Causes

Wrong domains.

## How to Fix

Add domains.

## Example

```javascript
// next.config.js
module.exports = { images: { remotePatterns: [{ hostname: 'example.com' }] } };
```
