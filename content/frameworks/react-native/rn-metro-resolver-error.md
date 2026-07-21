---
title: "[Solution] React Native Metro Module Resolver Error"
description: "react-native Metro cannot resolve a module path due to incorrect aliases, duplicate module versions, or misconfigured resolver settings"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Metro resolver error occurs when Metro cannot find a module that is imported in the source code. Unlike Node.js resolution, Metro uses its own resolver that is strict about extensions, duplicate versions, and platform-specific files.

## Common Causes

- Importing a module without the file extension that Metro can infer
- Two versions of the same library exist in node_modules (version conflit)
- Metro resolver fields in package.json pointing to a missing entry file
- Using yarn resolutions or npm overrides that point to an incompatible version
- Platform-specific file (.ios.js, .android.js) loaded on the wrong platform
- Misconfigured extraNodeModules or watchFolders in metro.config.js

## How to Fix

1. Clear Metro cache and node_modules:

```bash
npx react-native start --reset-cache
rm -rf node_modules && npm install
```

2. Ensure only one version of the conflicting library:

```json
// package.json
"resolutions": {
  "react-native-safe-area-context": "4.9.0"
}
```

3. Configure the resolver explicitly:

```javascript
// metro.config.js
const { getDefaultConfig, mergeConfig } = require('@react-native/metro-config');

const config = {
  resolver: {
    extraNodeModules: {
      '@app': `${__dirname}/src`,
    },
  },
};
```

## Examples

```bash
# Error: Unable to resolve module `some-package` from `src/App.js`
# Fix: check package.json for main entry
# If package.json has "main": "dist/index.js", that file must exist

# Alternative: map the path in metro.config.js
resolver: {
  resolveRequest: (context, moduleName, platform) => {
    if (moduleName === 'some-package') {
      return { type: 'sourceFile', filePath: '/path/to/dist/index.js' };
    }
    return context.resolveRequest(context, moduleName, platform);
  },
}
```

## Related Errors

- [Unable to Resolve Module]({{< relref "/frameworks/react-native/rn-unable-to-resolve-module" >}})
