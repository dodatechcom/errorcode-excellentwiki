---
title: "[Solution] ERR_MODULE_NOT_FOUND: module not found Error Fix"
description: "Fix Node.js ERR_MODULE_NOT_FOUND when importing ES modules. Resolve module resolution, file extensions, and package imports."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-module-not-found", "esm", "import", "module", "resolution"]
weight: 5
---

# ERR_MODULE_NOT_FOUND — module not found

This error occurs when Node.js cannot resolve an ES module import path. Unlike CommonJS, ES modules require exact file paths and extensions.

## What This Error Means

Common error messages:

- `Error [ERR_MODULE_NOT_FOUND]: Cannot find module '/path/to/module'`
- `ERR_MODULE_NOT_FOUND: Cannot find package 'lodash'`
- `Cannot find module './utils' imported from '/path/to/index.js'`

ES module resolution is stricter than CommonJS — it requires explicit file extensions and full paths.

## Common Causes

```javascript
// Cause 1: Missing file extension in ESM
import { foo } from './utils'; // ERR_MODULE_NOT_FOUND (needs .js)

// Cause 2: Missing package in node_modules
import express from 'express'; // if not installed

// Cause 3: Directory import without index.js
import config from './config'; // ESM doesn't resolve to config/index.js

// Cause 4: Typo in module path
import { bar } from './utlis'; // misspelled
```

## How to Fix

### Fix 1: Add file extensions for local imports

```javascript
// Wrong (ESM)
import { foo } from './utils';

// Correct (ESM)
import { foo } from './utils.js';
```

### Fix 2: Install missing packages

```bash
npm install express
# or
yarn add express
```

### Fix 3: Use full path for directory imports

```javascript
// Wrong (ESM doesn't resolve directories)
import config from './config';

// Correct
import config from './config/index.js';
```

### Fix 4: Configure import map for bare specifiers

```json
// package.json
{
  "imports": {
    "#utils": "./src/utils.js",
    "#config": "./src/config/index.js"
  }
}
```

```javascript
import { helper } from '#utils';
```

## Examples

```javascript
// This triggers ERR_MODULE_NOT_FOUND
// File: src/index.mjs
import { formatDate } from './helpers'; // Missing .js extension

// Fix:
import { formatDate } from './helpers.js';
```

## Related Errors

- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err-import-assertion" >}}) — require() of ES module
- [ERR_UNSUPPORTED_DIR_IMPORT]({{< relref "/languages/javascript/err-unsupported-dir-import" >}}) — directory import
- [ENOENT]({{< relref "/languages/javascript/enoent-node" >}}) — file not found
