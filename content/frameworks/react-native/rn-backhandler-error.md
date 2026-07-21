---
title: "[Solution] React Native BackHandler Error"
description: "Back button not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Back button not working.

## Common Causes

Not configured.

## How to Fix

Add listener.

## Example

```javascript
useEffect(() => {
  const b = BackHandler.addEventListener('hardwareBackPress', () => true);
  return () => b.remove();
}, []);
```
