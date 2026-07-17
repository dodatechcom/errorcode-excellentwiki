---
title: "Webpack Module Not Found Can't Resolve"
description: "Webpack cannot resolve a module or import path."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Module Not Found — Can't Resolve

This error occurs when Webpack cannot resolve a module or import path. The file may not exist, the path may be incorrect, or the file extension may be missing.

## Common Causes

- File does not exist at the specified path
- Import path is misspelled
- File extension not configured in resolve
- Symlinked paths not resolved
- Module not installed in node_modules

## How to Fix

### Check the Import Path

```bash
ls -la src/components/Header.jsx
```

### Add File Extensions to Resolve

```javascript
// webpack.config.js
module.exports = {
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'],
  },
};
```

### Configure Module Directories

```javascript
module.exports = {
  resolve: {
    modules: ['src', 'node_modules'],
  },
};
```

### Add Path Alias

```javascript
const path = require('path');

module.exports = {
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@components': path.resolve(__dirname, 'src/components'),
    },
  },
};
```

### Install Missing Module

```bash
npm install <module-name>
# or
yarn add <module-name>
```

### Fix Symlink Issues

```javascript
module.exports = {
  resolve: {
    symlinks: false,
  },
};
```

## Examples

```text
ERROR in ./src/App.js
Module not found: Error: Can't resolve './components/Header'
  in '/home/user/project/src'

ERROR in ./src/utils.js
Module not found: Error: Can't resolve 'lodash'
```

## Related Errors

- [Webpack Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
- [Webpack Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
- [Webpack Plugin Error]({{< relref "/tools/webpack/webpack-plugin-error" >}}) — plugin errors
