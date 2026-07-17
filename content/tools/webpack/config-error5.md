---
title: "[Solution] Webpack Invalid Configuration"
description: "Fix webpack configuration errors. Resolve invalid config syntax and schema validation issues."
tools: ["webpack"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Webpack Invalid Configuration

Webpack validates the configuration object against a JSON schema at startup. An invalid configuration error means a property is misspelled, has the wrong type, or is placed at the wrong level.

## Common Causes

- A property name is misspelled (e.g., `entry` as `entrty`)
- A property has the wrong type (e.g., a string where an array is expected)
- A deprecated option is used in the current webpack version
- The configuration object structure is incorrect

## How to Fix

### Run webpack with Full Error Output

```bash
npx webpack --config webpack.config.js 2>&1 | head -30
```

### Validate Configuration Manually

```bash
npx webpack --validate
```

### Check Common Configuration Structure

```javascript
// webpack.config.js
module.exports = {
  mode: 'development',          // 'development' | 'production' | 'none'
  entry: './src/index.js',      // string | object | array
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [],                  // array of rule objects
  },
  plugins: [],                  // array of plugin instances
};
```

### Fix Common Mistakes

```javascript
// WRONG: property at wrong level
module.exports = {
  entry: './src/index.js',
  filename: 'bundle.js',  // should be inside output
};

// CORRECT
module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
```

## Examples

```javascript
// Unknown property
module.exports = {
  entry: './src/index.js',
  watchOptions: {  // valid
    poll: true,
  },
  watchOptions2: {},  // ERROR: Unknown option
};

// Wrong type
module.exports = {
  entry: 123,  // ERROR: should be string or object
};
```

## Related Errors

- [Optimization Error]({{< relref "/tools/webpack/optimization-error" >}}) — optimization phase failure
- [HMR Error]({{< relref "/tools/webpack/hmr-error" >}}) — hot module replacement issue
