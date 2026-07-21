---
title: "[Solution] React useImperativeHandle Error"
description: "Error when useImperativeHandle is used incorrectly."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when useImperativeHandle is used incorrectly.

## Common Causes

Missing dependencies or not with forwardRef.

## How to Fix

Use with forwardRef and proper deps.

## Example

```javascript
const I = React.forwardRef(function I(p, r) {
  useImperativeHandle(r, () => ({ focus: () => {} }));
  return <input />;
});
```
