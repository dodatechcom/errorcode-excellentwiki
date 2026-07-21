---
title: "[Solution] Webpack Module Graph Unconnected"
description: "Fix Webpack module graph unconnected errors. Resolve issues when modules are not connected in the dependency graph."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Module Graph Unconnected

Fix Webpack module graph unconnected errors. Resolve issues when modules are not connected in the dependency graph.

## Common Causes

- Entry point is not defined or resolves to an empty module
- Dynamic import creates a detached sub-graph that is not reachable
- Module is excluded by a rule but still referenced by other modules
- SideEffects optimization prunes the module as unused code

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