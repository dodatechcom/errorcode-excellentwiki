---
title: "[Solution] Webpack CSS Extraction Error"
description: "Fix webpack CSS extraction errors when MiniCssExtractPlugin fails to extract styles into separate files during production builds."
tools: ["webpack"]
error-types: ["tool-error"]
severities: ["error"]
---

# Webpack CSS Extraction Error

MiniCssExtractPlugin extracts CSS into separate files. An extraction error occurs when the plugin cannot process CSS output from loaders, resulting in a build failure or missing styles in the output bundle.

## Common Causes

- The MiniCssExtractPlugin loader is used alongside style-loader in the same rule
- CSS contains syntax that the plugin cannot parse, such as unbalanced braces
- A PostCSS or Sass loader outputs an unexpected format
- The output filename pattern for CSS conflicts with the JavaScript pattern

## How to Fix

1. Ensure style-loader and MiniCssExtractPlugin loader are not used together:

```javascript
// Incorrect -- uses both loaders for the same rule
{
  test: /\.css$/,
  use: [MiniCssExtractPlugin.loader, 'style-loader', 'css-loader']
}

// Correct -- use only MiniCssExtractPlugin.loader
{
  test: /\.css$/,
  use: [MiniCssExtractPlugin.loader, 'css-loader']
}
```

2. Verify the plugin is added to the plugins array:

```javascript
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/[name].[contenthash].css'
    })
  ]
};
```

3. Check that the CSS output filename does not collide with JavaScript:

```javascript
new MiniCssExtractPlugin({
  filename: 'styles/[name].[contenthash].css', // separate directory
})
```

4. Validate the CSS output by running the build with verbose logging:

```bash
npx webpack --stats-error-details
```

## Examples

```bash
# Error output
ERROR in ./src/styles/main.css
Module build failed (from ./node_modules/mini-css-extract-plugin/dist/loader.js):
Error: You may not use a hyphenated class name in production
```

```javascript
// webpack.config.js with correct CSS extraction
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader']
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/[name].[contenthash:8].css'
    })
  ]
};
```

## Related Errors

- [CSS Loader]({{< relref "/tools/webpack/css-loader" >}}) -- CSS loader configuration issues
- [MiniCssExtractPlugin]({{< relref "/tools/webpack/minicssextractplugin" >}}) -- plugin-specific errors
