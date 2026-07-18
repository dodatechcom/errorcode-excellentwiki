---
title: "[Solution] JavaScript SWC Compiler Error — How to Fix"
description: "Fix JavaScript SWC compiler errors. Resolve configuration, transformation, and output issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 5
---

# JavaScript SWC Compiler Error

An `Error: SWC failed` or `TransformError` occurs when SWC fails to transform JavaScript code, encounters invalid syntax, or when the configuration is incompatible.

## Why It Happens

SWC is a fast JavaScript/TypeScript compiler. Errors arise when the input has syntax errors, when configuration options are incompatible, when plugins fail to transform, or when the output format is invalid.

## Common Error Messages

- `Error: Failed to compile`
- `Unexpected token in JSON`
- `Transform failed with N errors`
- `Cannot find module`

## How to Fix It

### Fix 1: Configure SWC properly

```javascript
// .swcrc
{
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "decorators": true
    },
    "transform": {
      "legacyDecorator": true,
      "decoratorMetadata": true
    },
    "target": "es2020"
  },
  "module": {
    "type": "commonjs"
  },
  "minify": true
}
```

### Fix 2: Handle TypeScript

```javascript
// Transform TypeScript
const swc = require('@swc/core');

async function transform(code) {
  try {
    const result = await swc.transform(code, {
      jsc: {
        parser: {
          syntax: 'typescript',
          tsx: true,
        },
        target: 'es2020',
      },
    });
    return result.code;
  } catch (error) {
    console.error('Transform failed:', error.message);
  }
}
```

### Fix 3: Use with bundler

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: {
          loader: 'swc-loader',
          options: {
            jsc: {
              parser: {
                syntax: 'typescript',
                tsx: true,
              },
            },
          },
        },
      },
    ],
  },
};
```

### Fix 4: Fix decorator issues

```javascript
// .swcrc
{
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "decorators": true
    },
    "transform": {
      "legacyDecorator": true,
      "decoratorMetadata": true
    }
  }
}
```

## Common Scenarios

- **Syntax error** — Input code has invalid JavaScript/TypeScript syntax.
- **Missing configuration** — Required parser options not specified.
- **Plugin conflict** — Multiple plugins produce incompatible output.

## Prevent It

- Always specify the correct `syntax` option for your source code.
- Use `jsc.target` to ensure output is compatible with your runtime.
- Test transformations with representative code samples.

## Related Errors

- [TransformError](/javascript/transform-error/) — transformation failed
- [SyntaxError](/javascript/syntaxerror/) — invalid input syntax
- [ConfigError](/javascript/config-error/) — invalid configuration
