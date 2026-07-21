---
title: "[Solution] React Too Many Re-renders"
description: "React error when a component triggers infinite re-renders."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

React error when a component triggers infinite re-renders.

## Common Causes

State updates happening during render.

## How to Fix

Move state updates into event handlers.

## Example

```jsx
function Counter() {
  const [c, setC] = useState(0);
  return <button onClick={() => setC(x => x + 1)}>{c}</button>;
}
```
