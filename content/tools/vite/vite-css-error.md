---
title: "Vite CSS Processing Error"
description: "Vite fails to process or transform CSS files."
tools: ["vite"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Vite CSS Processing Error

A Vite CSS processing error occurs when Vite fails to process, transform, or compile CSS files. Vite uses PostCSS for CSS processing and can integrate with preprocessors like Sass, Less, and Stylus.

## Common Causes

- Missing CSS preprocessor (Sass, Less)
- PostCSS plugin errors
- Invalid CSS syntax
- Missing CSS import dependencies

## How to Fix

### Install CSS Preprocessors

```bash
npm install --save-dev sass
# or
npm install --save-dev less
```

### Check CSS Syntax

```css
/* Invalid CSS */
.container {
  width: 100%
  height: 100vh
}

/* Valid CSS */
.container {
  width: 100%;
  height: 100vh;
}
```

### Configure PostCSS

```javascript
// vite.config.js
export default defineConfig({
  css: {
    postcss: {
      plugins: [
        require('autoprefixer'),
      ],
    },
  },
});
```

### Fix CSS Import Issues

```css
/* Ensure file exists */
@import './components/button.css';
@import 'normalize.css';
```

### Check Preprocessor Options

```javascript
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: '@import "./variables.scss";',
      },
    },
  },
});
```

## Examples

```bash
npx vite build
[vite:css] PostCSS syntax error
file: /src/styles.scss:5:3

# Fix: correct CSS syntax or install sass
npm install --save-dev sass
```

## Related Errors

- [Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — build failure
- [Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin error
- [Asset Error]({{< relref "/tools/vite/vite-asset-error" >}}) — asset processing error
