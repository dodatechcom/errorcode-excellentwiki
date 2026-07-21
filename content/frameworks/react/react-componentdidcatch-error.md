---
title: "[Solution] React componentDidCatch Error"
description: "Error in componentDidCatch lifecycle."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error in componentDidCatch lifecycle.

## Common Causes

Forgetting to update state.

## How to Fix

Use getDerivedStateFromError for fallback.

## Example

```javascript
class EB extends React.Component {
  componentDidCatch(e, i) { logError(e, i); }
}
```
