---
title: "Vite CSS PostCSS Error"
description: "Vite fails to process CSS files with PostCSS or CSS preprocessors."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite CSS — PostCSS Error

This error occurs when Vite fails to process CSS files with PostCSS or CSS preprocessors (SCSS, Sass, Less). The CSS pipeline encounters errors during compilation or transformation.

## Common Causes

- Missing PostCSS plugins
- Incorrect PostCSS configuration
- SCSS/Sass syntax errors
- Missing preprocessor dependencies
- `@import` paths not resolved

## How to Fix

### Install Required Dependencies

```bash
npm install -D postcss autoprefixer
# For SCSS
npm install -D sass
```

### Create PostCSS Config

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'),
  ],
};
```

### Configure CSS in Vite

```javascript
// vite.config.js
export default defineConfig({
  css: {
    postcss: './postcss.config.js',
    preprocessorOptions: {
      scss: {
        additionalData: `@import "./src/styles/variables.scss";`,
      },
    },
  },
});
```

### Fix SCSS Import Paths

```scss
/* src/styles/main.scss */
@use './variables' as *;  // modern Sass syntax
@import './components/button';
```

### Fix PostCSS Plugin Order

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('postcss-import'),   // must be first
    require('postcss-nested'),   // second
    require('autoprefixer'),     // last
  ],
};
```

### Add Tailwind CSS Support

```javascript
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

## Examples

```text
[vite] Internal server error: postcss-plugin errors:
  Syntax Error: Unexpected token at line 5 in main.scss
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
- [Vite React Error]({{< relref "/tools/vite/vite-react-error" >}}) — React JSX errors
