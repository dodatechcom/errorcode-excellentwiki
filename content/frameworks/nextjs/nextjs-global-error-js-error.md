---
title: "[Solution] Next.js Global Error JS Error"
description: "global-error.js not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

global-error.js not working.

## Common Causes

File missing.

## How to Fix

Create file.

## Example

```jsx
'use client';
export default function Error({ error, reset }) {
  return <div><h2>Global Error</h2><button onClick={reset}>Retry</button></div>;
}
```
