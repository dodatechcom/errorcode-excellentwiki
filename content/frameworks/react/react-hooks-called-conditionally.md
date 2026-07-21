---
title: "[Solution] React Hooks Called Conditionally"
description: "Error when React hooks are called inside conditions or loops."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when React hooks are called inside conditions or loops.

## Common Causes

Placing hooks inside if statements.

## How to Fix

Always call hooks at the top level.

## Example

```javascript
function Component({ show }) {
  const [d, setD] = useState(null);
  return show ? <div>{d}</div> : null;
}
```
