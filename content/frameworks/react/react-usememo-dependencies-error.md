---
title: "[Solution] React useMemo Dependencies Error"
description: "Warning when useMemo dependency array is wrong."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning when useMemo dependency array is wrong.

## Common Causes

Missing or excessive dependencies.

## How to Fix

Include only values used by computation.

## Example

```javascript
const s = useMemo(() => items.sort((a, b) => a.n - b.n), [items]);
```
