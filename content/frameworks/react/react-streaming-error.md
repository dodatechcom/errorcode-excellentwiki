---
title: "[Solution] React Streaming Error"
description: "Streaming not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Streaming not working.

## Common Causes

Not configured.

## How to Fix

Use Suspense.

## Example

```jsx
<Suspense fallback={<Loader />}><DataComponent /></Suspense>
```
