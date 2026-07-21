---
title: "[Solution] React Optimistic Update Error"
description: "Optimistic update not reverting."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Optimistic update not reverting.

## Common Causes

Wrong logic.

## How to Fix

Handle rollback.

## Example

```javascript
const [data, setData] = useState(initial);
// Optimistically update
setData(newData);
// On error, revert
```
