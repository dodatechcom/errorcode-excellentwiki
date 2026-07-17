---
title: "Loader Error in Webpack"
description: "A Webpack loader fails to process a module during the build."
tools: ["webpack"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Loader Error in Webpack

A loader error occurs when a configured loader (Babel, TypeScript, CSS, etc.) fails to process a module. The error identifies which loader failed and what transformation error occurred.

## Common Causes

- Loader version incompatible with the file type
- Missing loader dependencies (e.g., `@babel/preset-env`)
- Loader configuration errors in `webpack.config.js`
- Source file contains syntax the loader cannot parse

## How to Fix

### Check Loader Configuration

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],
          },
        },
      },
    ],
  },
};
```

### Install Missing Loader Dependencies

```bash
npm install --save-dev babel-loader @babel/core @babel/preset-env
```

### Fix TypeScript Loader Configuration

```javascript
{
  test: /\.tsx?$/,
  use: 'ts-loader',
  exclude: /node_modules/,
}
```

### Check for Conflicting Loaders

```javascript
// Ensure rule exclusion patterns don't overlap
{
  test: /\.js$/,
  exclude: /(node_modules|bower_components)/,
  use: 'babel-loader',
}
```

### Enable Loader Error Details

```bash
npx webpack --stats-error-details
```

## Examples

```bash
npx webpack
ERROR in ./src/app.jsx
Module build failed (from ./node_modules/babel-loader/lib/index.js):
SyntaxError: Unexpected token (10:5)

@ ./src/index.js 1:0-5
```

## Related Errors

- [Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
- [Module Not Found]({{< relref "/tools/webpack/webpack-module-not-found" >}}) — unresolved module
