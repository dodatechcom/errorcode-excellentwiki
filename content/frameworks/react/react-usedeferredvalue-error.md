---
title: "[Solution] React useDeferredValue Error"
description: "Stale display with useDeferredValue."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Stale display with useDeferredValue.

## Common Causes

Not using deferred value.

## How to Fix

Use for heavy rendering.

## Example

```javascript
function S({ q }) { const dq = useDeferredValue(q); return <Heavy q={dq} />; }
```
