---
title: "[Solution] Webpack Tree Shaking Not Working"
description: "Fix Webpack tree shaking not working errors. Resolve issues when unused exports are not eliminated."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Tree Shaking Not Working

Fix Webpack tree shaking not working errors. Resolve issues when unused exports are not eliminated.

## Common Causes

- Module is not marked as side-effect free in package.json
- Babel configuration transpiles ES modules to CommonJS format
- sideEffects setting is not configured in the webpack configuration
- Library uses dynamic exports that prevent static analysis

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