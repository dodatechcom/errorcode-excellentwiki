---
title: "Webpack Loader Error CSS Sass"
description: "Webpack loader fails while processing CSS, SCSS, or other style files."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Loader Error — CSS/Sass Processing

This error occurs when a webpack loader fails while processing CSS, SCSS, Sass, or other style files. The loader encounters invalid syntax or configuration issues.

## Common Causes

- Missing or misconfigured style loaders
- SCSS/Sass syntax errors
- Missing PostCSS configuration
- Incorrect loader order (loaders run right to left)
- Incorrect file path in @import

## How to Fix

### Install Required Loaders

```bash
npm install -D css-loader style-loader
npm install -D sass-loader node-sass
```

### Configure Style Loaders

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
```

### Fix SCSS Import Paths

```scss
/* Use relative path */
@import 'variables';

/* or configure includePaths */
// webpack.config.js
{
  loader: 'sass-loader',
  options: {
    sassOptions: {
      includePaths: ['src/styles'],
    },
  },
}
```

### Check Loader Order

```javascript
// Loaders execute right to left
use: [
  'style-loader',   // 3. Injects CSS into DOM
  'css-loader',     // 2. Resolves @import and url()
  'sass-loader',    // 1. Compiles SCSS to CSS
]
```

### Add PostCSS Configuration

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'),
  ],
};
```

## Examples

```text
ERROR in ./src/styles/main.scss
Module build failed (from ./node_modules/css-loader/dist/cjs.js):
CssSyntaxError: Unclosed bracket (2:1)

@import './variables'
^
```

## Related Errors

- [Webpack Build Error]({{< relref "/tools/webpack/webpack-build-error" >}}) — general build failure
- [Webpack Asset Error]({{< relref "/tools/webpack/webpack-asset-error" >}}) — asset processing failure
- [Webpack Config Error]({{< relref "/tools/webpack/webpack-config-error" >}}) — configuration error
