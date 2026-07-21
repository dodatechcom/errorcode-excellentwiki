---
title: "[Solution] Webpack Dev Server Port In Use"
description: "Fix Webpack dev server port in use errors. Resolve issues when the development server cannot start on the configured port."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Dev Server Port In Use

Fix Webpack dev server port in use errors. Resolve issues when the development server cannot start on the configured port.

## Common Causes

- Another process is already listening on the configured port number
- Previous dev server instance was not shut down cleanly
- Port range in the configuration is too narrow for concurrent usage
- Operating system has not released the port from a TIME_WAIT state

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