---
title: "[Solution] React Error Page Boundary Error"
description: "error.js not implemented."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

error.js not implemented.

## Common Causes

Missing error boundary.

## How to Fix

Create app/error.js.

## Example

```jsx
'use client';
export default function Error({ error, reset }) {
  return <div><h2>Error</h2><button onClick={reset}>Retry</button></div>;
}
```
