---
title: "[Solution] React getStaticPaths Error"
description: "getStaticPaths failing."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

getStaticPaths failing.

## Common Causes

Wrong format.

## How to Fix

Return paths.

## Example

```javascript
export async function getStaticPaths() {
  return { paths: [{ params: { id: '1' } }], fallback: false };
}
```
