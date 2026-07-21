---
title: "[Solution] Next.js Revalidate Error"
description: "Revalidation not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Revalidation not working.

## Common Causes

Wrong config.

## How to Fix

Set revalidate.

## Example

```javascript
const d = await fetch('...', { next: { revalidate: 3600 } });
```
