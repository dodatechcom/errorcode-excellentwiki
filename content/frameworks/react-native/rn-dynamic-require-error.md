---
title: "[Solution] React Native Dynamic require() is not supported"
description: "react-native Metro bundler does not support dynamic string expressions in require() or import() for JavaScript bundles"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The dynamic require error appears during Metro bundling when a file uses a variable inside require() or import() arguments. Metro performs static dependency discovery at build time, so runtime-dynamic paths cannot be resolved.

## Common Causes

- require(pathVariable) where pathVariable is not a string literal
- import(computedPath) with an expression that Metro cannot evaluate
- Async loading a file based on a server response
- Platform conditional require using a variable instead of Platform.select
- Requiring images with a variable string path

## How to Fix

1. Replace dynamic require with a static object mapping:

```javascript
// Bad: dynamic
const comp = require(componentName);

// Good: static map
const components = {
  Profile: require('./Profile').default,
  Settings: require('./Settings').default,
};
const Comp = components[componentName];
```

2. For assets and images, use a lookup object:

```javascript
const logoMap = {
  light: require('./light.png'),
  dark: require('./dark.png'),
};
<Image source={logoMap[theme]} />
```

for async chunks:

```javascript
// Bad: import(dynamicPath)
// Good: conditional static import
const Profile = Platform.select({
  ios: () => import('./Profile.ios'),
  android: () => import('./Profile.android'),
});
```

## Examples

```javascript
// Error: The provided argument did not evaluate to a string literal in require()
// Bad:
const path = './screens/' + screen + '.js';
const Screen = require(path);

// Fix:
const screens = {
  home: require('./screens/Home.js'),
  faq: require('./screens/FAQ.js'),
};
const Screen = screens[screen];
```

## Related Errors

- [Unable to Resolve Module]({{< relref "/frameworks/react-native/rn-unable-to-resolve-module" >}})
