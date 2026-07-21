---
title: "[Solution] Webpack HMR Update Failed"
description: "Fix Webpack hot module replacement update failed errors. Resolve issues when HMR does not apply changes."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack HMR Update Failed

Fix Webpack hot module replacement update failed errors. Resolve issues when HMR does not apply changes.

## Common Causes

- Module exports are not compatible with the HMR API
- Update manifest is stale or missing from the dev server output
- Client-side code does not accept the module update event
- CSS module is loaded via a plugin that does not support HMR

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