---
title: "[Solution] Webpack Hot Module Replacement Error"
description: "Fix webpack HMR errors. Resolve hot module replacement failures in development mode."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webpack", "hmr", "hot-module", "development", "reload"]
weight: 5
---

# Webpack Hot Module Replacement Error

An HMR error occurs when webpack's hot module replacement system fails to update modules in the browser without a full reload. The error may appear in the browser console or as a build warning.

## Common Causes

- The `HotModuleReplacementPlugin` is not added to the config
- The dev server is not configured to enable HMR
- A module does not accept HMR updates (missing `module.hot.accept`)
- The HMR socket connection to the dev server is lost

## How to Fix

### Enable HMR in devServer

```javascript
// webpack.config.js
module.exports = {
  devServer: {
    hot: true,
    // or use --hot flag: npx webpack serve --hot
  },
};
```

### Add HotModuleReplacementPlugin

```javascript
const webpack = require('webpack');

module.exports = {
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
  ],
};
```

### Add HMR Accept in Entry Files

```javascript
// src/index.js
if (module.hot) {
  module.hot.accept('./module.js', () => {
    // Re-execute when module.js changes
    const updatedModule = require('./module.js');
  });
}
```

### Use React Fast Refresh Instead

```bash
npm install --save-dev @pmmmwh/react-refresh-webpack-plugin react-refresh
```

## Examples

```javascript
// HMR not enabled
// [webpack-dev-server] Hot Module Replacement is disabled
// Fix: add hot: true to devServer config

// Module does not accept updates
// [HMR] Cannot check for circular dependencies
// Fix: add module.hot.accept() in the module
```

## Related Errors

- [Config Error]({{< relref "/tools/webpack/config-error5" >}}) — invalid webpack configuration
- [Dev Server Error]({{< relref "/tools/vite/dev-server-error" >}}) — Vite dev server issue
