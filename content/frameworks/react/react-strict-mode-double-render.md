---
title: "[Solution] React Strict Mode Double Render"
description: "Components rendering twice in development due to Strict Mode."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Components rendering twice in development due to Strict Mode.

## Common Causes

Intentional double rendering.

## How to Fix

This is expected in development.

## Example

```javascript
useEffect(() => {
  console.log('mount');
  return () => console.log('unmount');
}, []);
```
