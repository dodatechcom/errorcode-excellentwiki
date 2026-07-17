---
title: "Webpack ChunkLoadError Loading Chunk Failed"
description: "Webpack chunk fails to load at runtime."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack ChunkLoadError — Loading Chunk Failed

This error occurs when a webpack chunk fails to load at runtime, typically when using dynamic imports or code splitting. The browser cannot fetch the chunk file from the server.

## Common Causes

- Chunk file not deployed or missing from server
- Deployment occurred while user has old page loaded
- Network error fetching the chunk file
- Incorrect `publicPath` configuration
- Filename hash changed between builds

## How to Fix

### Configure Public Path

```javascript
// webpack.config.js
module.exports = {
  output: {
    publicPath: '/',
  },
};
```

### Use Error Boundaries for Dynamic Imports

```javascript
const Dashboard = React.lazy(() =>
  import('./Dashboard', {
    onError: (error) => {
      console.error('Chunk load failed:', error);
      // Redirect to fallback or reload
    },
  })
);
```

### Add Retry Logic for Chunk Loading

```javascript
function loadChunk(importFn) {
  return importFn().catch((error) => {
    if (error.name === 'ChunkLoadError') {
      return importFn(); // retry once
    }
    throw error;
  });
}
```

### Configure Output Filenames

```javascript
module.exports = {
  output: {
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].js',
  },
};
```

### Deploy All Assets Together

```bash
# Ensure all chunks are deployed atomically
rsync -av dist/ server:/var/www/app/
```

## Examples

```text
Uncaught (in promise) ChunkLoadError: Loading chunk 0 failed.
  at localhost:3000/dashboard:1:1
```

## Related Errors

- [Webpack Hot Reload Error]({{< relref "/tools/webpack/webpack-hot-reload-error" >}}) — HMR failures
- [Webpack Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
- [Webpack Dev Server Error]({{< relref "/tools/webpack/webpack-dev-server-error" >}}) — dev server issues
