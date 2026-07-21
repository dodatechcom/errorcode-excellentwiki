---
title: "[Solution] React This Binding Error"
description: "Class methods losing this context."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Class methods losing this context.

## Common Causes

Not binding methods.

## How to Fix

Use arrow functions or bind.

## Example

```javascript
class C extends React.Component {
  handleClick = () => { console.log(this.props); }
}
```
