---
title: "Webpack Plugin Error Undefined Is Not a Function"
description: "Webpack plugin throws an error during initialization or execution."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Plugin Error — Undefined Is Not a Function

This error occurs when a webpack plugin throws an error, often because the plugin is incompatible with the webpack version or its API has changed.

## Common Causes

- Plugin incompatible with webpack 5 API
- Plugin not installed or missing dependency
- Plugin constructor called incorrectly
- Plugin expects different webpack version
- Missing plugin configuration options

## How to Fix

### Verify Plugin Compatibility

```bash
npm ls webpack
npm ls <plugin-name>
```

### Update Plugin to Latest Version

```bash
npm install <plugin-name>@latest
```

### Check Plugin API Usage

```javascript
// webpack.config.js
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
  ],
};
```

### Fix Plugin Configuration

```javascript
// Wrong - missing required option
new CopyPlugin()

// Correct
new CopyPlugin({
  patterns: [
    { from: 'public', to: 'dist' },
  ],
})
```

### Use Compatible Plugin Versions

```javascript
// For webpack 5
npm install html-webpack-plugin@5

// For webpack 4
npm install html-webpack-plugin@4
```

### Check Plugin Documentation

```bash
npm info <plugin-name> version
# Check webpack compatibility in README
```

## Examples

```text
TypeError: plugin.apply is not a function
  at Compiler.apply (webpack/lib/Compiler.js:300:10)

TypeError: HtmlWebpackPlugin is not a constructor
  at module.exports (webpack.config.js:3:5)
```

## Related Errors

- [Webpack Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
- [Webpack Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
- [Webpack Module Not Found]({{< relref "/tools/webpack/webpack-module-not-found" >}}) — unresolved module
