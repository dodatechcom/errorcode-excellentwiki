---
title: "[Solution] React Suspense Loading Error"
description: "Suspense not showing fallback."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Suspense not showing fallback.

## Common Causes

Missing fallback.

## How to Fix

Add fallback.

## Example

```jsx
<Suspense fallback={<Loader />}><DataComponent /></Suspense>
```
