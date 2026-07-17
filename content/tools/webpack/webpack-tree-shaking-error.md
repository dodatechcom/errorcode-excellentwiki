---
title: "Webpack Tree Shaking Warning"
description: "Webpack produces warnings about tree shaking and unused exports."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webpack", "tree-shaking", "dead-code", "optimization", "esm"]
weight: 5
---

# Webpack — Tree Shaking Warning

This error occurs when webpack detects issues with tree shaking. Modules may not be tree-shakeable due to CommonJS usage, side effects, or incorrect configuration.

## Common Causes

- Using CommonJS `require()` instead of ES modules `import`
- Package marked with `"sideEffects": true`
- Webpack not configured for production mode
- Barrel exports preventing dead code elimination

## How to Fix

### Enable Production Mode

```javascript
module.exports = {
  mode: 'production',
};
```

### Mark Side-Effect-Free Modules

```json
{
  "sideEffects": false
}
```

### Mark Specific Side-Effect Files

```json
{
  "sideEffects": ["*.css", "./src/polyfills.js"]
}
```

### Use ES Modules

```javascript
// Instead of CommonJS
// const { formatDate } = require('./utils');

// Use ES modules
import { formatDate } from './utils';
```

### Configure Used Exports

```javascript
module.exports = {
  optimization: {
    usedExports: true,
  },
};
```

### Analyze Bundle Size

```bash
npx webpack-bundle-analyzer stats.json
```

## Examples

```text
[webpack] Used exports from ./src/utils.js:
  WARNING in ./src/utils.js
  Module with side effects: ./src/utils.js
  The exports were not used and will be removed
```

## Related Errors

- [Webpack Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
- [Webpack Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
- [Webpack Asset Error]({{< relref "/tools/webpack/webpack-asset-error" >}}) — asset processing failure
