---
title: "[Solution] Webpack Module Build Failed"
description: "Fix webpack 'Module build failed' loader errors. Resolve loader configuration and processing issues."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Module Build Failed

A module build failed error means a loader encountered an error while transforming a module. The loader threw an exception or returned a failure during processing.

## Common Causes

- A loader configuration option is invalid
- The loader itself has a bug or is incompatible with the current webpack version
- A PostCSS plugin or Babel plugin is failing during transformation
- A required dependency for the loader is missing

## How to Fix

### Identify the Failing Loader

```
Module build failed (from ./node_modules/babel-loader/lib/index.js):
SyntaxError: Unexpected token
```

### Run with Verbose Logging

```bash
npx webpack --stats-error-details
```

### Fix Loader Configuration

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
```

### Check Loader Dependencies

```bash
npm ls css-loader style-loader
npm install --save-dev css-loader style-loader
```

### Fix Babel Plugin Issues

```json
// babel.config.json
{
  "presets": ["@babel/preset-env"],
  "plugins": ["@babel/plugin-transform-runtime"]
}
```

## Examples

```javascript
// css-loader not installed
// Module build failed (from ./node_modules/css-loader/lib/index.js)
// Fix: npm install --save-dev css-loader

// Incorrect loader order
rules: [{ test: /\.css$/, use: ['css-loader', 'style-loader'] }]
// loaders are applied right-to-left; wrong order causes errors
// Fix: use: ['style-loader', 'css-loader']
```

## Related Errors

- [Syntax Error]({{< relref "/tools/webpack/syntax-error9" >}}) — module parse failed
- [Optimization Error]({{< relref "/tools/webpack/optimization-error" >}}) — optimization phase failure
