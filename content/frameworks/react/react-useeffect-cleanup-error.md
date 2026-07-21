---
title: "[Solution] React useEffect Cleanup Error"
description: "Error when useEffect cleanup function returns incorrectly."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when useEffect cleanup function returns incorrectly.

## Common Causes

Returning a cleanup that throws.

## How to Fix

Return a function from useEffect for cleanup.

## Example

```javascript
useEffect(() => {
  const t = setInterval(() => {}, 1000);
  return () => clearInterval(t);
}, []);
```
