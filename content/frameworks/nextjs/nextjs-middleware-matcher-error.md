---
title: "[Solution] Next.js Middleware Matcher Error"
description: "Middleware not matching."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware not matching.

## Common Causes

Wrong matcher.

## How to Fix

Set matcher.

## Example

```javascript
export const config = { matcher: ['/api/:path*'] };
```
