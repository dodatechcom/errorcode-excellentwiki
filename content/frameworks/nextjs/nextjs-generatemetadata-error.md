---
title: "[Solution] Next.js generateMetadata Error"
description: "Dynamic metadata failing."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Dynamic metadata failing.

## Common Causes

Wrong function.

## How to Fix

Export function.

## Example

```javascript
export async function generateMetadata({ params }) {
  return { title: `Page ${params.id}` };
}
```
