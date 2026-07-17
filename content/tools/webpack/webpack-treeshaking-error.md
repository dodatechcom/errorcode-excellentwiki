---
title: "Tree Shaking Error in Webpack"
description: "Webpack tree shaking fails or produces incorrect results, causing missing exports."
tools: ["webpack"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Tree Shaking Error in Webpack

Tree shaking errors occur when Webpack incorrectly removes or keeps code during dead code elimination. This can cause missing exports or incorrect bundle output.

## Common Causes

- Using CommonJS modules instead of ES modules
- Package has no `sideEffects` field in `package.json`
- Incorrectly marking packages as side-effect free
- Module re-exports that confuse tree shaking

## How to Fix

### Ensure ES Module Usage

```javascript
// Good: ES modules (tree-shakeable)
export const myFunction = () => {};
import { myFunction } from './utils';

// Bad: CommonJS (NOT tree-shakeable)
module.exports = { myFunction };
const { myFunction } = require('./utils');
```

### Set sideEffects in package.json

```json
{
  "sideEffects": false
}
```

### Mark Specific Side Effects

```json
{
  "sideEffects": ["*.css", "*.scss", "./src/polyfills.js"]
}
```

### Enable Production Mode

```javascript
// webpack.config.js
module.exports = {
  mode: 'production',  // Enables tree shaking
  optimization: {
    usedExports: true,
  },
};
```

### Check Bundle Size

```bash
npx webpack --mode production --stats-modules-space 20
```

### Verify Tree Shaking Works

```bash
npx webpack --mode production 2>&1 | grep "inner modules"
```

## Examples

```bash
# Bundle includes unused exports
npx webpack --mode production
# Check bundle for dead code:
grep -c "console.log" dist/bundle.js  # Should be 0 in production
```

## Related Errors

- [Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — build failure
- [Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
- [Asset Error]({{< relref "/tools/webpack/webpack-asset-error" >}}) — asset processing error
