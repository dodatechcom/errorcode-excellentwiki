---
title: "[Solution] Next.js Catch All Routes Error"
description: "Catch all not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Catch all not working.

## Common Causes

Wrong syntax.

## How to Fix

Use [...slug].

## Example

```jsx
// app/blog/[...slug]/page.js
export default function Page({ params }) { return <div>{params.slug}</div>; }
```
