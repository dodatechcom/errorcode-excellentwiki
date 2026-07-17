---
title: "[Solution] ERR_REQUIRE_ESM: require() of ES module Error Fix"
description: "Fix Node.js ERR_REQUIRE_ESM when using require() on ES modules. Convert to ESM, use dynamic import, or configure package.json type field."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ERR_REQUIRE_ESM — require() of ES module

This error occurs when trying to use `require()` to load a module that only supports ES module syntax (import/export). Node.js CJS and ESM have different module systems.

## What This Error Means

Common error messages:

- `Error [ERR_REQUIRE_ESM]: require() of ES Module ... not supported`
- `ERR_REQUIRE_ESM: require() of ES Module '/path/to/module.mjs' not supported`
- `Cannot use import statement outside a module`

ES modules (`.mjs` or `"type": "module"` in package.json) cannot be loaded with `require()`. You must use `import` or dynamic `import()`.

## Common Causes

```javascript
// Cause 1: require() an ES module
const lodash = require('lodash-es'); // ERR_REQUIRE_ESM

// Cause 2: require() a .mjs file
const utils = require('./utils.mjs'); // ERR_REQUIRE_ESM

// Cause 3: Package.json has "type": "module"
// package.json: { "type": "module" }
// But using require() in code

// Cause 4: New version of dependency switched to ESM
// Previously worked with require(), now ESM-only
```

## How to Fix

### Fix 1: Use dynamic import()

```javascript
// Instead of require()
const lodash = await import('lodash-es');

// Or with default export
const { default: lodash } = await import('lodash-es');
```

### Fix 2: Convert project to ESM

```json
// package.json
{
  "type": "module"
}
```

```javascript
// index.js (ESM)
import express from 'express';
import { readFileSync } from 'fs';
const app = express();
```

### Fix 3: Use createRequire for ESM packages

```javascript
import { createRequire } from 'module';
const require = createRequire(import.meta.url);

const lodash = require('lodash-es');
```

### Fix 4: Use .cjs extension for CommonJS files

```json
// package.json
{
  "type": "module"
}
```

```javascript
// legacy.cjs (CommonJS in ESM project)
const express = require('express');
module.exports = { app };
```

## Examples

```javascript
// This triggers ERR_REQUIRE_ESM
// package.json: { "type": "module" }
// module.mjs: export const foo = 'bar';
const module = require('./module.mjs');

// Fix: use import
const module = await import('./module.mjs');
console.log(module.foo); // 'bar'
```

## Related Errors

- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-module-not-found" >}}) — module not found
- [ERR_UNSUPPORTED_DIR_IMPORT]({{< relref "/languages/javascript/err-unsupported-dir-import" >}}) — directory import
- [ModuleNotFoundError]({{< relref "/languages/javascript/modulenotfounderror" >}}) — module not found
