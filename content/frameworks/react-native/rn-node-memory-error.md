---
title: "[Solution] React Native Node.js Memory Exhausted"
description: "react-native Metro or Node.js process runs out of memory during build or development, killing the bundler process on large-scale projects"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Node.js memory exhausted error occurs when the Metro bundler or npm/yarn process exceeds the default Node.js memory limit (512MB or 1GB). This is common in large React Native projects with thousands of files in node_modules.

## Common Causes

- Project has too many files in node_modules due to hoisted monorepo
- Source maps generation consumes extra memory for large bundles
- TypeScript type checking inside the Metro process
- React Native version 0.70+ with Hermes source maps enabled
- ESLint or Prettier running in Node.js with increased memory usage
- Metro transformer holds all modules in memory simultaneously

## How to Fix

1. Increase Node.js memory limit:

```bash
# Increase to 4GB
NODE_OPTIONS="--max-old-space-size=4096" npx react-native start
```

2. Disable inline source maps in production:

```bash
NODE_OPTIONS="--max-old-space-size=4096" npx react-native bundle --platform android --dev false --inline-source-map false
```

3. Use Metro's transformer optimizations:

```javascript
// metro.config.js
const { getDefaultConfig, mergeConfig } = require('@react-native/metro-config');
const config = {
  transformer: {
    minifierConfig: {
      mangle: {
        reserved: [],
      },
    },
  },
};
```

## Examples

```bash
# Error: FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory
# Fix:
export NODE_OPTIONS=--max-old-space-size=4096
npx react-native run-android
```

## Related Errors

- [Metro Bundler Failed]({{< relref "/frameworks/react-native/rn-metro-bundler-failed" >}})
