---
title: "[Solution] React Native LogBox Not Showing Warnings"
description: "react-native LogBox fails to display console.warn or console.error messages in debug builds on Android and iOS in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The LogBox display error occurs when warnings and errors that should appear in the LogBox overlay do not show up. Since React Native 0.63, LogBox replaced the old YellowBox, but it can be suppressed or misconfigured.

## Common Causes

- LogBox.ignoreAllLogs(true) called in production or debug by accident
- console.disableYellowBox set to true (legacy flag still active)
- LogBox is hidden behind another modal or full-screen component
- Not importing LogBox from react-native in navigation guard files
- jsEngine is set to Hermes and console methods are stubbed out

## How to Fix

1. Check LogBox configuration:

```javascript
import { LogBox } from 'react-native';

// Make sure ignoreAllLogs is not true
LogBox.ignoreLogs(['Warning: ...']); // selective ignore
```

2. Ensure LogBox is not disabled via global flag:

```javascript
// Remove any legacy suppress flags
global.console.disableYellowBox = undefined;
// or set to false
global.console.disableYellowBox = false;
```

3. Force LogBox to show all logs in development:

```javascript
if (__DEV__) {
  LogBox.ignoreLogs([]); // clear all ignores in dev
}
```

## Examples

```javascript
// Error: warnings silently hidden
// console.warn('Something bad') does not show in LogBox

// Fix: check your index.js
import { LogBox } from 'react-native';
// Remove LogBox.ignoreAllLogs() if present
```

## Related Errors

- [Yellow Box Warning]({{< relref "/frameworks/react-native/rn-yellow-box-warning" >}})
