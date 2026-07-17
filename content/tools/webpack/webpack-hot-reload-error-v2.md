---
title: "Webpack HMR Hot Module Replacement Failed"
description: "Webpack hot module replacement fails during development."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webpack", "hmr", "hot", "module-replacement", "dev"]
weight: 5
---

# Webpack HMR — Hot Module Replacement Failed

This error occurs when webpack's Hot Module Replacement (HMR) fails to update modules in the browser during development. Changes are not reflected without a full page reload.

## Common Causes

- HMR not enabled or configured incorrectly
- Module does not support hot updates
- WebSocket connection lost
- Bundle entry point not set up for HMR
- Error in module code prevents HMR

## How to Fix

### Enable HMR in Dev Server

```javascript
// webpack.config.js
module.exports = {
  devServer: {
    hot: true,
  },
};
```

### Add HMR Entry Point

```javascript
module.exports = {
  entry: {
    main: [
      'webpack-dev-server/client?http://localhost:8080',
      'webpack/hot/only-dev-server',
      './src/index.js',
    ],
  },
};
```

### Add HMR Plugin

```javascript
const webpack = require('webpack');

module.exports = {
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
  ],
};
```

### Fix Module HMR Accept

```javascript
// src/index.js
if (module.hot) {
  module.hot.accept('./component', () => {
    // Re-render with new module
    render();
  });
}
```

### Check WebSocket Connection

```bash
# Ensure dev server is running and WebSocket is accessible
curl -i http://localhost:8080/sockjs-node/info
```

## Examples

```text
[HMR] The following modules failed to accept the update:
  - ./src/app.js
[HMR] Update failed: ChunkLoadError: Loading hot update failed
```

## Related Errors

- [Webpack Dev Server Error]({{< relref "/tools/webpack/webpack-dev-server-error" >}}) — dev server issues
- [Webpack Chunk Error]({{< relref "/tools/webpack/webpack-chunk-error" >}}) — chunk loading failure
- [Webpack Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
