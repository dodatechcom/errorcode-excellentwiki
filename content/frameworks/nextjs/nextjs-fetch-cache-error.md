---
title: "[Solution] Next.js Fetch Cache Error"
description: "Fetch not caching."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Fetch not caching.

## Common Causes

Wrong cache option.

## How to Fix

Set cache.

## Example

```javascript
const d = await fetch('...', { cache: 'force-cache' });
```
