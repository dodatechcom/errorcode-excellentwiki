---
title: "[Solution] Webpack Optimization Error"
description: "Fix webpack optimization errors. Resolve code splitting, minification, and tree shaking failures."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Optimization Error

An optimization error occurs when webpack's optimization phase fails. This includes code splitting, minification, tree shaking, and chunk creation failures.

## Common Causes

- A plugin in the optimization phase throws an error
- Minification (Terser) fails due to unsupported syntax in the source
- Code splitting encounters circular dependencies
- The `splitChunks` configuration is invalid

## How to Fix

### Disable Minification Temporarily

```javascript
// webpack.config.js
module.exports = {
  optimization: {
    minimize: false,
  },
};
```

### Fix Terser Configuration

```javascript
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  optimization: {
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: false,
        },
      }),
    ],
  },
};
```

### Fix splitChunks Configuration

```javascript
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      minSize: 20000,
      maxSize: 244000,
    },
  },
};
```

### Check for Circular Dependencies

```bash
npx webpack --stats-optimization-bailout
```

## Examples

```javascript
// Terser fails on unsupported syntax
// ERROR: Unexpected token: name 'yield'
// Fix: configure TerserPlugin to handle the syntax

// Invalid splitChunks config
// ERROR: optimization.splitChunks should be {Boolean|Object}
// Fix: ensure splitChunks is an object or boolean
```

## Related Errors

- [Loaders Error]({{< relref "/tools/webpack/loaders-error" >}}) — module build failed
- [Config Error]({{< relref "/tools/webpack/config-error5" >}}) — invalid webpack configuration
