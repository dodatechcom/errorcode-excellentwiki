---
title: "[Solution] Next.js Error JS Boundary Error"
description: "error.js not catching."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

error.js not catching.

## Common Causes

File missing.

## How to Fix

Create error.js.

## Example

```jsx
'use client';
export default function Error({ error, reset }) {
  return <div><h2>Error</h2><button onClick={reset}>Retry</button></div>;
}
```
