---
title: "[Solution] React Dynamic Route Error"
description: "Dynamic route not matching."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Dynamic route not matching.

## Common Causes

Wrong file naming.

## How to Fix

Use [param] syntax.

## Example

```jsx
// app/user/[id]/page.js
export default function Page({ params }) { return <div>{params.id}</div>; }
```
