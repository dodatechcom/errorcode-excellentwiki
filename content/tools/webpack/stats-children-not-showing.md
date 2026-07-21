---
title: "[Solution] Webpack Stats Children Not Showing"
description: "Fix Webpack stats children not showing errors. Resolve issues when child compiler stats are hidden."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Stats Children Not Showing

Fix Webpack stats children not showing errors. Resolve issues when child compiler stats are hidden.

## Common Causes

- stats.children option is set to false hiding all child output
- Child compiler is running inside a loader but not emitting output
- Stats preset does not include the children property
- Multiple child compilers write to the same stats object causing conflicts

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