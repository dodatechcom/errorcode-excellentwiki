---
title: "[Solution] ERR_UNSUPPORTED_DIR_IMPORT: directory import Error Fix"
description: "Fix Node.js ERR_UNSUPPORTED_DIR_IMPORT when importing directories in ES modules. Resolve directory imports with full paths or import maps."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-unsupported-dir-import", "directory-import", "esm", "import", "index"]
weight: 5
---

# ERR_UNSUPPORTED_DIR_IMPORT — directory import

This error occurs when importing a directory in ES modules without specifying the full path to the entry file. ES modules do not automatically resolve directory imports to `index.js`.

## What This Error Means

Common error messages:

- `Error [ERR_UNSUPPORTED_DIR_IMPORT]: Directory import '/path/to/utils' is not supported`
- `ERR_UNSUPPORTED_DIR_IMPORT: Importing directory './components' is not supported`

Unlike CommonJS (which resolves `./utils` to `./utils/index.js`), ES modules require explicit file paths.

## Common Causes

```javascript
// Cause 1: Importing a directory without /index.js
import { helper } from './utils'; // ERR_UNSUPPORTED_DIR_IMPORT

// Cause 2: Missing index.js in target directory
// ./components/index.js doesn't exist
import { Button } from './components'; // error

// Cause 3: Bare specifier resolving to a directory
import { something } from 'my-package'; // package main is a directory
```

## How to Fix

### Fix 1: Import the index file directly

```javascript
// Wrong
import { helper } from './utils';

// Correct
import { helper } from './utils/index.js';
```

### Fix 2: Use package.json exports field

```json
{
  "name": "my-package",
  "exports": {
    ".": "./src/index.js",
    "./utils": "./src/utils/index.js",
    "./components/*": "./src/components/*/index.js"
  }
}
```

```javascript
import { helper } from 'my-package/utils';
```

### Fix 3: Use import maps

```json
// package.json
{
  "imports": {
    "./utils": "./src/utils/index.js",
    "./components": "./src/components/index.js"
  }
}
```

```javascript
import { helper } from '#utils';
```

### Fix 4: Use webpack/vite resolve aliases

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
    },
  },
});
```

## Examples

```javascript
// Project structure:
// src/
//   components/
//     index.js
//     Button.js

// This triggers ERR_UNSUPPORTED_DIR_IMPORT
import { Button } from './components';

// Fix: import index directly
import { Button } from './components/index.js';
```

## Related Errors

- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-module-not-found" >}}) — module not found
- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err-import-assertion" >}}) — require() of ES module
- [ERR_UNKNOWN_FILE_EXTENSION]({{< relref "/languages/javascript/err_unknown_file_extension" >}}) — unknown file extension
