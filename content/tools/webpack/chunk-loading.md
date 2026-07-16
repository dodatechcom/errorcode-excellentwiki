---
title: "ChunkLoadError: Loading Chunk Failed"
description: "A dynamically loaded chunk failed to load at runtime, typically due to a missing file or incorrect public path."
tools: ["webpack"]
error-types: ["build-error"]
severities: ["error"]
tags: ["webpack", "chunk", "dynamic-import", "runtime"]
weight: 5
---

This runtime error occurs when a dynamically imported module (code-split chunk) cannot be loaded. The browser receives a 404 or network error when requesting the chunk file.

## Common Causes

- The chunk file was not included in the build output
- The `publicPath` configuration does not match where chunks are served
- A deployment overwrote old chunks but the HTML still references them
- CDN or server cache is stale and serving outdated asset manifests

## How to Fix

Set the correct `publicPath` in your webpack config:

```javascript
module.exports = {
  output: {
    publicPath: 'https://cdn.example.com/assets/',
  },
};
```

Ensure `chunkFilename` is configured for dynamic imports:

```javascript
module.exports = {
  output: {
    chunkFilename: '[name].[contenthash].chunk.js',
  },
};
```

Add error handling for failed dynamic imports:

```javascript
import(
  /* webpackChunkName: "dashboard" */
  './Dashboard'
).catch((err) => {
  console.error('Failed to load chunk:', err);
});
```

## Examples

```
Uncaught (in promise) ChunkLoadError: Loading chunk 42 failed.
(missing: https://cdn.example.com/assets/42.a1b2c3d4.chunk.js)
```

## Related Errors

- [Module Not Found]({{< relref "/tools/webpack/module-not-found" >}})
