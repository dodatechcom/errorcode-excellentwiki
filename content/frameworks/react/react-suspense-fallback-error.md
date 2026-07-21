---
title: "[Solution] React Suspense Fallback Error"
description: "Error when Suspense fallback is not properly defined."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when Suspense fallback is not properly defined.

## Common Causes

Missing fallback prop.

## How to Fix

Provide a valid React element as fallback.

## Example

```jsx
<Suspense fallback={<Loading />}><Lazy /></Suspense>
```
