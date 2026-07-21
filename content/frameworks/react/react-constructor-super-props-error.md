---
title: "[Solution] React Constructor super() Props Error"
description: "Forgetting to call super(props)."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Forgetting to call super(props).

## Common Causes

Not passing props to super().

## How to Fix

Always call super(props).

## Example

```javascript
class C extends React.Component {
  constructor(p) { super(p); }
}
```
