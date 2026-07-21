---
title: "[Solution] React Native Deep Linking Error"
description: "Deep link not handled."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Deep link not handled.

## Common Causes

Not configured.

## How to Fix

Configure linking.

## Example

```javascript
const linking = { prefixes: ['myapp://'], config: { screens: { Home: 'home' } } };
<NavigationContainer linking={linking}>
```
