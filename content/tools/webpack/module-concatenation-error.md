---
title: "[Solution] Webpack Module Concatenation Error"
description: "Fix webpack module concatenation scope hoisting errors when ScopeHoistingPlugin fails during the build optimization phase."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack Module Concatenation Error

Module concatenation, also known as scope hoisting, attempts to merge multiple modules into a single function scope to reduce bundle size and improve runtime performance. This error occurs when webpack cannot safely concatenate modules due to structural constraints.

## Common Causes

- A module uses `eval()` or dynamic `require()` that prevents static analysis
- CommonJS and ES module syntax are mixed within the same dependency chain
- A module exports multiple values using `module.exports` in a non-standard way
- The `ConcatenationPlugin` encounters circular dependencies in the module graph

## How to Fix

1. Disable module concatenation temporarily to identify the problematic module:

```javascript
// webpack.config.js
module.exports = {
  optimization: {
    concatenateModules: false
  }
};
```

2. Enable verbose output to find which modules fail concatenation:

```javascript
module.exports = {
  optimization: {
    concatenateModules: true
  },
  stats: {
    optimizationBailout: true
  }
};
```

3. Fix mixed module syntax by converting CommonJS to ES modules:

```javascript
// Before (CommonJS) -- causes concatenation issues
module.exports = { helper: () => {} };

// After (ES module) -- concatenation safe
export const helper = () => {};
```

4. Exclude specific modules from concatenation:

```javascript
module.exports = {
  optimization: {
    concatenateModules: true,
    providedExports: true
  }
};
```

## Examples

```bash
# Build with optimization bailout info
npx webpack --stats-optimization-bailout
# Output shows: ModuleConcatenationPlugin bailout: Scope hoisting is not possible
#   for module './src/legacy.js' because of eval()
```

```javascript
// webpack.config.js with concatenation diagnostics
module.exports = {
  mode: 'production',
  optimization: {
    concatenateModules: true,
    usedExports: true
  },
  stats: {
    optimizationBailout: true,
    errorDetails: true
  }
};
```

## Related Errors

- [Optimization Error]({{< relref "/tools/webpack/optimization-error" >}}) -- general optimization failures
- [Tree Shaking Error]({{< relref "/tools/webpack/webpack-tree-shaking-error" >}}) -- tree shaking failures
