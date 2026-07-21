---
title: "[Solution] React Native Hooks State Update Error"
description: "react-native hooks must be called in the same order on every render, and state updates after unmount cause React warning in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The hooks state error manifests as React warnings about changing the order of hooks from one render to the next, or setState being called on an unmounted component. Both are common issues in React Native due to race conditions with effects.

## Common Causes

- Conditional hooks placed after a return statement
- Using setState inside an async callback after component unmount
- Different number of hooks on initial render versus subsequent renders
- Hook called inside a nested function or if block that may not execute
- Memory leak from setState setInterval not cleared

## How to Fix

1. Never call hooks conditionally:

```javascript
// Bad: conditional hook
if (user) {
  const [name, setName] = useState(user.name); // RUNTIME ERROR
}

// Good: always call the same hooks
const [name, setName] = useState(user?.name ?? '');
```

2. Guard against unmounted state updates:

```javascript
useEffect(() => {
  let cancelled = false;
  fetchData().then(data => {
    if (!cancelled) {
      setState(data);
    }
  });
  return () => { cancelled = true; };
}, []);
```

3. Use cleanup to prevent memory leaks:

```javascript
useEffect(() => {
  const interval = setInterval(tick, 1000);
  return () => clearInterval(interval);
}, []);
```

## Examples

```javascript
// Error: Rendered more hooks than during the previous render
function App() {
 if (active) return <Other />; // early return
 const [val, setVal] = useState(0); // this hook moved after early return
}
// Fix: put all hooks before any early return
```

## Related Errors

- [Memory Leak Error]({{< relref "/frameworks/react-native/rn-memory-leak-error" >}})
- [TypeError Undefined Object]({{< relref "/frameworks/react-native/rn-typeerror-undefined-object" >}})
