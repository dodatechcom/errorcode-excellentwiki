---
title: "[Solution] React Missing Dependencies in useEffect"
description: "Warning about missing dependencies in useEffect dependency array."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning about missing dependencies in useEffect dependency array.

## Common Causes

Incomplete dependency arrays causing stale closures.

## How to Fix

Include all referenced variables.

## Example

```javascript
useEffect(() => { fetchData(userId); }, [userId]);
```
