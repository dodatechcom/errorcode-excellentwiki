---
title: "[Solution] Webpack Loader Options Deprecated"
description: "Fix Webpack loader options deprecated warnings. Resolve issues when loaders use obsolete configuration format."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Loader Options Deprecated

Fix Webpack loader options deprecated warnings. Resolve issues when loaders use obsolete configuration format.

## Common Causes

- Loader options passed directly to the rule instead of via options key
- Top-level configuration uses query string syntax which is deprecated
- Loader reads options from the wrong location in the rule definition
- Migration from webpack 4 to 5 changed the options format for loaders

## How to Fix

### Update webpack.config.js

Verify your webpack configuration includes the correct settings for this feature.

```javascript
// webpack.config.js
module.exports = {
  // Ensure correct configuration
  mode: 'production',
  // ... other options
};
```

### Clear the Build Cache

Delete node_modules/.cache and the output directory, then rebuild.

```bash
rm -rf node_modules/.cache dist
npx webpack --config webpack.config.js
```

### Check Loader and Plugin Versions

Ensure all loaders and plugins are compatible with the installed Webpack version.

```bash
npm ls webpack
npm ls webpack-cli
```

### Review Build Output

Analyze the build output for warnings and errors that indicate the root cause.

## Examples

```javascript
// webpack.config.js - Example fix
module.exports = {
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx'],
  },
};
```