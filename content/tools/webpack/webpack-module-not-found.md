---
title: "Module Not Found — Webpack"
description: "Webpack cannot resolve a module import, indicating a missing file or package."
tools: ["webpack"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Module Not Found — Webpack

This error means Webpack traced an import statement but could not find the corresponding file or installed package. The module path in the error points to the unresolved import.

## Common Causes

- The package is not installed (missing from `node_modules`)
- The import path contains a typo or incorrect casing
- A path alias is not configured in `webpack.config.js`
- The package has no `main` or `exports` field

## How to Fix

### Install Missing Package

```bash
npm install <package-name>
```

### Check for Typos in Import Path

```bash
ls -la src/components/MyComponent.jsx
```

### Configure Path Aliases

```javascript
const path = require('path');

module.exports = {
  resolve: {
    alias: {
      '@components': path.resolve(__dirname, 'src/components'),
      '@utils': path.resolve(__dirname, 'src/utils'),
    },
    extensions: ['.js', '.jsx', '.ts', '.tsx'],
  },
};
```

### Check package.json Main Field

```bash
node -e "console.log(require.resolve('package-name'))"
```

### Verify Module Exports

```bash
ls node_modules/package-name/
cat node_modules/package-name/package.json | grep -E '"main"|"exports"'
```

### Clear Module Resolution Cache

```bash
rm -rf node_modules/.cache/
npm install
```

## Examples

```bash
npx webpack
Module not found: Error: Can't resolve './components/Header' in '/app/src'

 @ ./src/App.js 1:0-42
```

## Related Errors

- [Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
- [Loader Error]({{< relref "/tools/webpack/loader-error" >}}) — loader processing failure
