---
title: "[Solution] Webpack No Exports Found"
description: "Fix Webpack no exports found errors. Resolve issues when importing from a module that has no exports."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack No Exports Found

Fix Webpack no exports found errors. Resolve issues when importing from a module that has no exports.

## Common Causes

- Module file does not export any symbols or default value
- Named import references a function that does not exist in the module
- Re-export barrel file is empty after tree shaking removed all symbols
- Default import is used on a module that only has named exports

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