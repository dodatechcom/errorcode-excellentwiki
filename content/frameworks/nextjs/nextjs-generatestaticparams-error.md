---
title: "[Solution] Next.js generateStaticParams Error"
description: "Static params generation failing."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Static params generation failing.

## Common Causes

Wrong return format.

## How to Fix

Return array.

## Example

```javascript
export function generateStaticParams() { return [{ id: '1' }, { id: '2' }]; }
```
