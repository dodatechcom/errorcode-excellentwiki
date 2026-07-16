---
title: "[Solution] Webpack Module Parse Failed"
description: "Fix webpack 'Module parse failed' syntax errors. Resolve loader and syntax issues in bundled modules."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["webpack", "syntax", "parse", "module", "loader"]
weight: 5
---

# Webpack Module Parse Failed

A module parse failed error means webpack's JavaScript parser could not understand a file. This happens when the file contains syntax that the parser does not support, or when a required loader is not configured.

## Common Causes

- The file uses syntax (e.g., JSX, TypeScript, optional chaining) without the required loader
- A loader is missing or misconfigured for that file type
- The file contains syntax not supported by the configured parser
- An incorrect `exclude` or `include` rule skips necessary files

## How to Fix

### Add the Required Loader

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
      {
        test: /\.ts$/,
        use: 'ts-loader',
      },
    ],
  },
};
```

### Install Missing Loaders

```bash
npm install --save-dev babel-loader @babel/core @babel/preset-env
```

### Configure Babel Presets

```json
// babel.config.json
{
  "presets": [
    ["@babel/preset-env", { "targets": "> 0.25%, not dead" }],
    "@babel/preset-react"
  ]
}
```

### Check the Error for the Unparseable Line

```
Module parse failed: Unexpected token (3:10)
You may need an appropriate loader to handle this file type.
```

## Examples

```javascript
// JSX without babel-loader
const el = <div>Hello</div>;
// ERROR: Module parse failed: Unexpected token

// TypeScript without ts-loader
const name: string = "world";
// ERROR: Module parse failed: Unexpected token
```

## Related Errors

- [Loaders Error]({{< relref "/tools/webpack/loaders-error" >}}) — module build failed
- [Syntax Error]({{< relref "/tools/webpack/syntax-error9" >}}) — related syntax issues
