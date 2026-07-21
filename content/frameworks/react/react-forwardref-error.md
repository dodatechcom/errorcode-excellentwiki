---
title: "[Solution] React forwardRef Error"
description: "Error when using React.forwardRef incorrectly."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when using React.forwardRef incorrectly.

## Common Causes

Not wrapping component with forwardRef.

## How to Fix

Use forwardRef to expose child refs.

## Example

```javascript
const I = React.forwardRef(function I(p, r) {
  return <input ref={r} {...p} />;
});
```
