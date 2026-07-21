---
title: "[Solution] React Invalid Hook Call Error"
description: "Error when hooks are called outside a React function component."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when hooks are called outside a React function component.

## Common Causes

Calling hooks from non-component functions.

## How to Fix

Only call hooks from React function components.

## Example

```javascript
function useData() {
  const [d, setD] = useState([]);
  return d;
}
```
