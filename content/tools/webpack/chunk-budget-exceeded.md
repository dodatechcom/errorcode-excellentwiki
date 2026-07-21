---
title: "[Solution] Webpack Chunk Budget Exceeded"
description: "Fix Webpack chunk budget exceeded errors. Resolve issues when bundle size exceeds configured limits."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Chunk Budget Exceeded

Fix Webpack chunk budget exceeded errors. Resolve issues when bundle size exceeds configured limits.

## Common Causes

- Performance budget is set too low for the application size
- Large library imported without tree-shaking or code splitting
- Asset size exceeds the maxAssetSize in the performance configuration
- Multiple copies of the same library bundled into one chunk

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