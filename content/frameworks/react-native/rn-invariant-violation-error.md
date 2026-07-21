---
title: "[Solution] React Native Invariant Violation Error"
description: "react-native Invariant Violation due to duplicate root view, incorrect component name, or missing default exported component in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Invariant Violation is a generic React Native error that typically indicates a structural problem with the component tree: multiple App components rendered, wrong module name in AppRegistry, or component that has no default export.

## Common Causes

- AppRegistry.registerComponent called more than once
- The registered component name does not match the native side
- Root component file exports multiple items and the named export is used
- Multiple React roots created by calling AppRegistry.runApplication multiple times
- A component's render returned undefined or null unexpectedly

## How to Fix

1. Verify the App registration:

```javascript
// index.js
import { AppRegistry } from 'react-native';
import App from './App';
import { name as appName } from './app.json';

// name must match app.json
AppRegistry.registerComponent(appName, () => App);
```

2. Check for duplicate registrations when using code push:

```javascript
if (!AppRegistry.registerComponent) {
  AppRegistry.registerComponent(appName, () => App);
}
```

3. Ensure the component is a class or function:

```javascript
// Ensure App is not undefined
const App = () => <View />;
export default App;
```

## Examples

```javascript
// Error: Invariant Violation: "Element type is invalid: expected a string or a class/function but got undefined..."
// Fix: Check the import path and export name
import App from './App'; // default export
// vs
import { App } from './components'; // named export
```

## Related Errors

- [TypeError]({{< relref "/frameworks/react-native/rn-typeerror-undefined-object" >}})
- [RedBox Error]({{< relref "/frameworks/react-native/rn-redbox-error" >}})
