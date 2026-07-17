---
title: "Metro bundler error"
description: "React Native Metro bundler throws errors when it cannot bundle the JavaScript code"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["metro", "bundler", "bundle", "hot-reload", "module"]
weight: 5
---

This error occurs when Metro bundler fails to bundle the JavaScript code for the React Native application. It can happen during development or when building a release bundle.

## Common Causes

- JavaScript syntax errors in the codebase
- Import path is incorrect or file does not exist
- Metro cache is corrupted
- Port 8081 already in use by another process
- Module resolution conflicts in `metro.config.js`

## How to Fix

1. Reset Metro cache and restart:

```bash
npx react-native start --reset-cache
```

2. Kill any existing Metro processes:

```bash
# Find and kill Metro process on port 8081
lsof -ti:8081 | xargs kill -9
```

3. Configure Metro properly:

```js
// metro.config.js
const { getDefaultConfig } = require('metro-config');

module.exports = (async () => {
  const defaultConfig = await getDefaultConfig();
  return {
    resolver: {
      sourceExts: [...defaultConfig.resolver.sourceExts, 'svg'],
    },
    transformer: {
      getTransformOptions: async () => ({
        transform: {
          experimentalImportSupport: true,
          inlineRequires: true,
        },
      }),
    },
  };
})();
```

4. Fix import resolution:

```javascript
// Wrong
import Component from './Component';

// Correct — verify file exists
import Component from './components/Component';
```

## Examples

```bash
# Metro error — module not found
error: bundling failed Error: Unable to resolve module `./utils/formatDate`
```

## Related Errors

- [RedBox error]({{< relref "/frameworks/react-native/red-box-error" >}})
- [Hermes error]({{< relref "/frameworks/react-native/hermes-error" >}})
