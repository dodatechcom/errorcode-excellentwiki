---
title: "[Solution] React useLayoutEffect vs useEffect"
description: "Using useLayoutEffect incorrectly causing perf issues."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Using useLayoutEffect incorrectly causing perf issues.

## Common Causes

Using useLayoutEffect for heavy computations.

## How to Fix

Use useLayoutEffect only for DOM measurements.

## Example

```javascript
useLayoutEffect(() => { setH(ref.current.offsetHeight); }, []);
```
