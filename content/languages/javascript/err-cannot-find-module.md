---
title: "[Solution] Node.js ERR_MODULE_NOT_FOUND — Cannot Find Module Fix"
description: "Fix Node.js ERR_MODULE_NOT_FOUND when a required module cannot be found. Resolve module resolution errors in Node.js applications."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_MODULE_NOT_FOUND — Cannot Find Module Fix

The `ERR_MODULE_NOT_FOUND` error occurs when Node.js cannot locate a required module. This happens when the module path is incorrect, the module is not installed, or the module resolution algorithm fails to find the target.

## Description

Common ERR_MODULE_NOT_FOUND messages include:

- `Cannot find module 'module-name'` — module not in node_modules or path.
- `ERR_MODULE_NOT_FOUND: Cannot find module '/path/to/module.js'` — specific file not found.
- `Cannot find module './relative-path'` — relative path resolution failed.
- `Module not found: Error: Can't resolve 'module-name'` — webpack/bundler error.

## Common Causes

```javascript
// Cause 1: Module not installed
const express = require("express"); // ERR_MODULE_NOT_FOUND if not in node_modules

// Cause 2: Typo in module name
const expresss = require("expresss"); // typo

// Cause 3: Wrong relative path
const utils = require("./utils"); // ERR_MODULE_NOT_FOUND if file doesn't exist

// Cause 4: ESM/CJS mismatch
import myModule from "./my-module.cjs"; // ERR_MODULE_NOT_FOUND for ESM
```

## Solutions

### Fix 1: Install missing dependencies

```bash
# Install the missing module
npm install module-name

# Or for dev dependencies
npm install --save-dev module-name

# Check if module exists in package.json
cat package.json | grep module-name
```

### Fix 2: Verify module path

```javascript
const path = require("node:path");
const fs = require("node:fs");

function requireSafe(modulePath) {
  const resolved = path.resolve(__dirname, modulePath);
  if (!fs.existsSync(resolved)) {
    throw new Error(`Module not found: ${resolved}`);
  }
  return require(resolved);
}

// Usage
const myModule = requireSafe("./lib/my-module");
```

### Fix 3: Check file extension for ESM

```javascript
// When using ES modules, specify file extensions
import { myFunc } from "./utils.js"; // correct
import { myFunc } from "./utils"; // ERR_MODULE_NOT_FOUND

// Or configure in package.json
// package.json: { "type": "module" }
```

### Fix 4: Set up proper module resolution

```javascript
// Use module-alias for path aliasing
// npm install module-alias --save

// package.json
{
  "_moduleAliases": {
    "@utils": "./src/utils",
    "@lib": "./src/lib"
  }
}

// In entry file
require("module-alias/register");

// Then use aliases
const utils = require("@utils/helper");
```

## Examples

```javascript
// ERR_MODULE_NOT_FOUND when npm install was not run
// After cloning a repo, you must install dependencies:
// $ npm install

const express = require("express");
// Error: Cannot find module 'express'
// Install it: npm install express

// ERR_MODULE_NOT_FOUND with wrong path
const config = require("./config");
// Error: Cannot find module './config'
// Check the actual path: ls -la ./config*
// Maybe it's ./config.js or ./config/index.js
```

## Related Errors

- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — require() used on ES module.
- [ERR_UNKNOWN_FILE_EXTENSION]({{< relref "/languages/javascript/err_unknown_file_extension" >}}) — unknown file extension.
- [ERR_UNSUPPORTED_ESM_URL_SCHEME]({{< relref "/languages/javascript/err_unsupported_esm_url_scheme" >}}) — unsupported ESM URL scheme.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/ERR_MODULE_NOT_FOUND" >}}) — existing page for this error.
