---
title: "Chunk Loading Error — Webpack"
description: "Webpack chunk fails to load at runtime, causing application errors."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webpack", "chunk", "loading", "runtime", "code-splitting"]
weight: 5
---

# Chunk Loading Error — Webpack

A chunk loading error occurs when a dynamically imported module chunk fails to load at runtime. This typically happens with code splitting when chunks cannot be fetched from the server.

## Common Causes

- Chunk file not available on the server (deployment timing issue)
- Public path configuration is incorrect
- Server returns 404 for chunk files
- CORS issues preventing chunk loading
- Chunk filename changed after deployment

## How to Fix

### Set Correct Public Path

```javascript
// webpack.config.js
module.exports = {
  output: {
    publicPath: '/',
    // Or use dynamic public path
    publicPath: 'auto',
  },
};
```

### Use Dynamic Import for Code Splitting

```javascript
// Use webpack magic comments for chunk naming
const Module = React.lazy(() => import(/* webpackChunkName: "module" */ './Module'));
```

### Handle Chunk Loading Errors

```javascript
// Retry failed chunk loads
window.addEventListener('error', (event) => {
  if (event.message.includes('ChunkLoadError')) {
    window.location.reload();
  }
});
```

### Ensure All Chunks Are Deployed

```bash
# After build, verify chunk files exist in dist/
ls dist/*.js
```

### Configure Output Filenames for Caching

```javascript
module.exports = {
  output: {
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].chunk.js',
  },
};
```

## Examples

```javascript
// Runtime error
Uncaught (in promise) ChunkLoadError: Loading chunk 4 failed.
(missing: http://localhost:3000/4.chunk.js)
```

## Related Errors

- [Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — build failure
- [Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
