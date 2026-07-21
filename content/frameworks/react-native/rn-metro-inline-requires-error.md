---
title: "[Solution] React Native Metro Inline Requires Error"
description: "react-native Metro bundler errors when inline requires optimization fails to transform dynamic imports or lazy requires in production bundles"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Metro inline requires error occurs when the Metro bundler is configured to inline require calls but encounters a dynamic require that cannot be transformed. Inline requires are enabled by default in production to speed up startup by deferring module loading.

## Common Causes

- Metro config sets inlineRequires: true but a module uses dynamic require
- A third-party library uses var x = require('mod') in a function body
- Circular dependency prevents Metro from inlining the require safely
- Mixing import and require in the same file causes transform order issues
- Using require inside a try-catch where the module path is not static

## How to Fix

1. Check Metro config for inline requires:

```javascript
// metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
};
```

2. Disable inline requires if a library breaks:

```javascript
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        inlineRequires: { blockList: { 'some-module': true } },
      },
    }),
  },
};
```

3. Convert dynamic require to static import in your code:

```javascript
// Bad
function loadModule(name) {
  return require('./modules/' + name);
}
// Good
const modules = {
  home: require('./modules/home'),
  profile: require('./modules/profile'),
};
```

## Examples

```javascript
// Error: Requiring unknown module "undefined"
// caused by inline requires not resolving dynamic path

// Fix: disable inline requires for the problematic path
inlineRequires: { blockList: { './src/screens': true } }
```

## Related Errors

- [Transform Error]({{< relref "/frameworks/react-native/rn-transform-error" >}})
- [Dynamic Require Error]({{< relref "/frameworks/react-native/rn-dynamic-require-error" >}})
