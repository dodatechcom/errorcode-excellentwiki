---
title: "[Solution] Next.js Async Component Error"
description: "Async server component failing."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Async server component failing.

## Common Causes

Wrong usage.

## How to Fix

Use await.

## Example

```jsx
async function Page() {
  const d = await getData();
  return <div>{d.title}</div>;
}
```
