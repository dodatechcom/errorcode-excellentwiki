---
title: "Hot Module Replacement Error — Webpack"
description: "Webpack HMR fails to update modules in the development server."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webpack", "hmr", "hot-module", "development", "reload"]
weight: 5
---

# Hot Module Replacement Error — Webpack

A Hot Module Replacement (HMR) error occurs when Webpack's development server cannot update modules in place. Instead of a full page reload, HMR tries to swap modules but fails.

## Common Causes

- HMR is not enabled in webpack config
- Module cannot be hot-replaced (non-replaceable exports)
- WebSocket connection to dev server lost
- Module has side effects that prevent replacement
- Code syntax error prevents HMR update

## How to Fix

### Enable HMR

```javascript
// webpack.config.js
module.exports = {
  devServer: {
    hot: true,
    // Enable for CSS
    hotOnly: true,
  },
};
```

### Add HMR Entry

```javascript
module.exports = {
  entry: {
    app: ['webpack-dev-server/client?http://localhost:8080', 'webpack/hot/only-dev-server', './src/index.js'],
  },
};
```

### Use Accept API

```javascript
// In modules that support HMR
if (module.hot) {
  module.hot.accept('./utils', () => {
    // Re-execute module
  });
  module.hot.dispose(() => {
    // Cleanup before replacement
  });
}
```

### Fix Non-Replaceable Exports

```javascript
// Only default exports and specific named exports can be hot-replaced
// Convert named exports to default export if possible
export default { fn1, fn2 };
```

### Check WebSocket Connection

```bash
# Ensure dev server is running
npx webpack serve --hot
```

## Examples

```javascript
// Console error
[HMR] Update failed: Error: Aborted because there is no acceptance handler
for ./src/utils.js in {0}

// Fix: add HMR accept handler
if (module.hot) {
  module.hot.accept('./utils', () => {});
}
```

## Related Errors

- [Dev Server Error]({{< relref "/tools/webpack/webpack-dev-server-error" >}}) — dev server issues
- [Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — build failure
