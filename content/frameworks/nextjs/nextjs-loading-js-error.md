---
title: "[Solution] Next.js Loading JS Error"
description: "loading.js not showing."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

loading.js not showing.

## Common Causes

File missing.

## How to Fix

Create loading.js.

## Example

```jsx
// app/loading.js
export default function Loading() { return <div>Loading...</div>; }
```
