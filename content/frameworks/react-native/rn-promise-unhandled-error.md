---
title: "[Solution] React Native Unhandled Promise Rejection Error"
description: "react-native unhandled promise rejection causing YellowBox warning or crashing the app due to async errors not being caught in React Native"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The unhandled promise rejection error occurs when a Promise fails (rejects) and there is no .catch() handler attached. React Native surfaces these as yellow warnings in development and can crash the app in production if the rejection reaches the global event loop.

## Common Causes

- Async function called without await or .catch()
- fetch() call with no error handling for network failures
- await expression in a function that is not itself async
- Promise.all() where one promise rejects and there is no global rejection handler
- Third-party library that returns a promise which is not consumed
- Missing try-catch around async code in useEffect

## How to Fix

1. Always attach a catch handler:

```javascript
// Bad
fetch(url).then(setData);

// Good
fetch(url)
  .then(setData)
  .catch(error => console.error('Fetch failed:', error));
```

2. Use try-catch with async/await:

```javascript
useEffect(() => {
  const loadData = async () => {
    try {
      const data = await fetchData();
      setData(data);
    } catch (err) {
      setError(err.message);
    }
  };
  loadData();
}, []);
```

3. Set a global rejection handler:

```javascript
// In index.js
if (__DEV__) {
  const rejections = new Set();
  const onRejection = (event) => {
    rejections.add(event.reason);
    console.warn('Unhandled Promise rejection:', event.reason);
  };
  window.addEventListener('unhandledrejection', onRejection);
}
```

## Examples

```javascript
// Error: Possible Unhandled Promise Rejection (id: 0):
// TypeError: Network request failed

// Fix: add .catch on every fetch
fetch(url).then(res => res.json()).catch(err => setError(err));
```

## Related Errors

- [Network Error]({{< relref "/frameworks/react-native/rn-network-error" >}})
