---
title: "[Solution] React State Update on Unmounted Component"
description: "Warning about updating state on an unmounted component."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning about updating state on an unmounted component.

## Common Causes

Async operations completing after component unmount.

## How to Fix

Cancel async operations in useEffect cleanup.

## Example

```javascript
useEffect(() => {
  const c = new AbortController();
  fetchData({ signal: c.signal });
  return () => c.abort();
}, []);
```
