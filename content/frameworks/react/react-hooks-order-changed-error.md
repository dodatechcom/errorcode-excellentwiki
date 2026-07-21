---
title: "[Solution] React Hooks Order Changed Error"
description: "React error when the number or order of hooks changes."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

React error when the number or order of hooks changes.

## Common Causes

Conditional returns before hooks.

## How to Fix

Ensure all hooks are called in the same order.

## Example

```javascript
function Component({ items }) {
  const [sel, setSel] = useState(null);
  if (items.length === 0) return null;
  return <div>{sel}</div>;
}
```
