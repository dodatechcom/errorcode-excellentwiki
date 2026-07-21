---
title: "[Solution] Webpack Dev Server History API Fallback"
description: "Fix Webpack dev server history API fallback errors. Resolve issues when SPA routing returns 404."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Dev Server History API Fallback

Fix Webpack dev server history API fallback errors. Resolve issues when SPA routing returns 404.

## Common Causes

- HistoryApiFallback is not enabled in the dev server options
- Rewrite rules do not match the URL path being requested
- Index file is not set correctly and defaults to the wrong file
- Multiple HTML entry points confuse the fallback configuration

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