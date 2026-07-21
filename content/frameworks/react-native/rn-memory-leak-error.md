---
title: "[Solution] react-native Memory Leak Error"
description: "App memory growing."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

App memory growing.

## Common Causes

Not cleaning up.

## How to Fix

Remove listeners.

## Example

```javascript
useEffect(() => {
  const sub = EventEmitter.addListener('event', handler);
  return () => sub.remove();
}, []);
```
