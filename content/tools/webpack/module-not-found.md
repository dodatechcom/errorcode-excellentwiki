---
title: "Module Not Found: Can't Resolve Module"
description: "webpack cannot resolve a module import, indicating a missing file, package, or misconfigured resolver."
tools: ["webpack"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error means webpack traced an import statement but could not find the corresponding file or installed package. The module path in the error points to the unresolved import.

## Common Causes

- The package is not installed (missing from `node_modules`)
- The import path contains a typo or incorrect casing
- A path alias or resolver alias is not configured in `webpack.config.js`
- The package is installed but has no `main` or `exports` field

## How to Fix

Install the missing package:

```bash
npm install <package-name>
```

Check for typos in the import path and verify the file exists:

```bash
ls -la src/components/MyComponent.jsx
```

If using path aliases, configure the resolver in `webpack.config.js`:

```javascript
const path = require('path');

module.exports = {
  resolve: {
    alias: {
      '@components': path.resolve(__dirname, 'src/components'),
    },
    extensions: ['.js', '.jsx', '.ts', '.tsx'],
  },
};
```

## Examples

```
Module not found: Error: Can't resolve './components/Header' in '/app/src'

 @ ./src/App.js 1:0-42
```

## Related Errors

- [Chunk Loading]({{< relref "/tools/webpack/chunk-loading" >}})
