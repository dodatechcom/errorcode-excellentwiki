---
title: "[Solution] React Context Provider Missing"
description: "Warning when context value is undefined because no Provider is rendered."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning when context value is undefined because no Provider is rendered.

## Common Causes

Forgot to wrap with Provider.

## How to Fix

Wrap component tree with Context.Provider.

## Example

```jsx
function App() {
  return <MyContext.Provider value={v}><Child /></MyContext.Provider>;
}
```
