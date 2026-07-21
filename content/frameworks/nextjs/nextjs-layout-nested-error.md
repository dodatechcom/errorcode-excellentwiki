---
title: "[Solution] Next.js Layout Nested Error"
description: "Nested layout not rendering."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Nested layout not rendering.

## Common Causes

Missing layout.js.

## How to Fix

Create layout file.

## Example

```jsx
// app/dashboard/layout.js
export default function DashLayout({ children }) {
  return <div><Sidebar />{children}</div>;
}
```
