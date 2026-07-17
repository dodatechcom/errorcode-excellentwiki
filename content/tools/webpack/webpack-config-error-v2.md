---
title: "Webpack Invalid Configuration Object"
description: "Webpack rejects the configuration object due to invalid options."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Invalid Configuration Object

This error occurs when the webpack configuration object does not match the expected schema. Invalid option names, types, or values cause webpack to reject the configuration.

## Common Causes

- Misspelled configuration property names
- Wrong value types (e.g., string where array expected)
- Deprecated configuration options
- Unknown top-level properties
- Conflicting configuration options

## How to Fix

### Validate Configuration Schema

```bash
npx webpack --validate
```

### Check Configuration Properties

```javascript
// webpack.config.js
module.exports = {
  mode: 'production',          // correct
  entry: './src/index.js',     // correct
  output: {
    filename: 'bundle.js',     // correct
    path: __dirname + '/dist', // correct
  },
};
```

### Fix Value Types

```javascript
// Wrong - entry must be string, array, or object
entry: 123,

// Correct
entry: './src/index.js',
// or
entry: ['./src/index.js', './src/vendor.js'],
```

### Remove Deprecated Options

```javascript
// Deprecated
module.exports = {
  plugins: [],
  module: {
    rules: []
  }
};

// Use mode instead of deprecated UglifyJsPlugin
module.exports = {
  mode: 'production', // replaces UglifyJsPlugin
};
```

### Check for Typos

```javascript
// Wrong
module.exports = {
  outptu: { filename: 'bundle.js' },  // typo
};

// Correct
module.exports = {
  output: { filename: 'bundle.js' },
};
```

## Examples

```text
Invalid configuration object. Webpack has been initialized
using a configuration object that does not match the API schema.
 - configuration.output has an unknown property 'publicPathd'.
```

## Related Errors

- [Webpack Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
- [Webpack Dev Server Error]({{< relref "/tools/webpack/webpack-dev-server-error" >}}) — dev server issues
- [Webpack Plugin Error]({{< relref "/tools/webpack/webpack-plugin-error" >}}) — plugin errors
