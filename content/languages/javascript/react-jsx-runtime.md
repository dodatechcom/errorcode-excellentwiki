---
title: "[Solution] React JSX Runtime Not Found Error Fix"
description: "Fix React JSX runtime errors when the JSX transform cannot be found. Configure Babel, TypeScript, and bundler settings for JSX."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["react", "jsx", "runtime", "babel", "transform", "new-jsx"]
weight: 5
---

# React JSX Runtime Not Found

This error occurs when the bundler or runtime cannot locate the `jsx-runtime` module needed to transform JSX syntax. It is common when migrating to the new JSX transform.

## What This Error Means

Common error messages:

- `Module not found: Error: Can't resolve 'react/jsx-runtime'`
- `Cannot find module 'react/jsx-runtime'`
- `JSX runtime not found`

React 17+ introduced the new JSX transform which requires `react/jsx-runtime`. Older setups use `React.createElement` instead.

## Common Causes

```javascript
// Cause 1: Missing react/jsx-runtime in node_modules
// React version too old (< 17.0.0)

// Cause 2: Wrong babel config
// Missing @babel/plugin-transform-react-jsx

// Cause 3: TypeScript config issues
// "jsx": "react" instead of "react-jsx"

// Cause 4: Bundler not configured for new JSX transform
```

## How to Fix

### Fix 1: Update React version

```bash
npm install react@latest react-dom@latest
```

### Fix 2: Configure TypeScript for new JSX

```json
// tsconfig.json
{
  "compilerOptions": {
    "jsx": "react-jsx"
  }
}
```

### Fix 3: Configure Babel

```json
// babel.config.json
{
  "presets": [
    ["@babel/preset-react", {
      "runtime": "automatic"
    }]
  ]
}
```

### Fix 4: Configure Vite

```javascript
// vite.config.js
import react from '@vitejs/plugin-react';

export default {
  plugins: [react()],
};
```

### Fix 5: Configure webpack

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [{
      test: /\.jsx?$/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: [
            ['@babel/preset-react', { runtime: 'automatic' }],
          ],
        },
      },
    }],
  },
};
```

## Examples

```bash
# Check if react/jsx-runtime exists
ls node_modules/react/jsx-runtime*

# If missing, React is too old
npm install react@18
```

```typescript
// tsconfig.json fix
{
  "compilerOptions": {
    "jsx": "react-jsx",  // not "react"
    "esModuleInterop": true
  }
}
```

## Related Errors

- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-module-not-found" >}}) — module not found
- [Babel Error]({{< relref "/languages/javascript/babel-error" >}}) — babel transpilation
- [TypeScript Compilation Error]({{< relref "/languages/javascript/ts-loader-error" >}}) — TS compilation
