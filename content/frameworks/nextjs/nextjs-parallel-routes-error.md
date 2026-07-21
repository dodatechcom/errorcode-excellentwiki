---
title: "[Solution] Next.js Parallel Routes Error"
description: "Parallel routes not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Parallel routes not working.

## Common Causes

Slots not defined.

## How to Fix

Create slot files.

## Example

```jsx
// app/layout.js
export default function Layout({ children, analytics }) {
  return <div>{children}{analytics}</div>;
}
```
