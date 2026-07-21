---
title: "[Solution] React Error Boundary Catch Error"
description: "Error boundaries not catching errors in async code."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error boundaries not catching errors in async code.

## Common Causes

Boundaries only catch render errors.

## How to Fix

Use try/catch in event handlers.

## Example

```javascript
class EB extends React.Component {
  state = { e: false };
  static getDerivedStateFromError() { return { e: true }; }
  render() { return this.state.e ? <h1>Err</h1> : this.props.children; }
}
```
