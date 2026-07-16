---
title: "[Solution] Node.js ERR_MODULE_NOT_FOUND — ESM Module Resolution Fix"
description: "Fix Node.js ERR_MODULE_NOT_FOUND for ES module imports. Add file extensions, fix package.json exports, and resolve import paths correctly."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-module-not-found", "esm", "import", "module-resolution", "nodejs"]
weight: 5
---

# Node.js ERR_MODULE_NOT_FOUND — ESM Module Resolution Fix

The `ERR_MODULE_NOT_FOUND` error occurs when Node.js ESM loader cannot resolve an import path. Unlike CommonJS `require()`, ESM `import` requires explicit file extensions, does not auto-resolve directories, and is influenced by the `exports` field in `package.json`. This is distinct from the CommonJS `MODULE_NOT_FOUND` error.

## Description

Common ERR_MODULE_NOT_FOUND messages include:

- `ERR_MODULE_NOT_FOUND: Cannot find package 'X' imported from 'Y'` — package not installed or not resolvable.
- `ERR_MODULE_NOT_FOUND: Cannot find module './utils' imported from '/app/src/index.js'` — missing file extension.
- `ERR_MODULE_NOT_FOUND: Cannot find module './config'` — directory import not supported in ESM.

## Common Causes

```javascript
// Cause 1: Missing file extension in relative import
import { helper } from "./utils";  // ERR_MODULE_NOT_FOUND — should be "./utils.js"

// Cause 2: Directory import not supported
import { db } from "./models";  // ERR_MODULE_NOT_FOUND — need "./models/index.js"

// Cause 3: Package not installed
import express from "express";  // ERR_MODULE_NOT_FOUND if not in node_modules

// Cause 4: Package "exports" field blocks the import path
import helper from "my-package/src/helper.js";  // ERR_PACKAGE_PATH_NOT_EXPORTED
```

## Solutions

### Fix 1: Add explicit file extensions to relative imports

```javascript
// Wrong — ESM requires explicit extensions
import { helper } from "./utils";
import { db } from "./models/connection";

// Correct — include the file extension
import { helper } from "./utils.js";
import { db } from "./models/connection.js";
```

### Fix 2: Import specific files instead of directories

```javascript
// Wrong — directory import not supported in ESM
import { User } from "./models";

// Correct — import the specific file
import { User } from "./models/user.js";
```

### Fix 3: Configure package.json for ESM

```json
{
  "name": "my-app",
  "type": "module",
  "main": "./src/index.js"
}
```

```javascript
// .mjs files are always treated as ESM regardless of package.json
import express from "express";
export const handler = (req, res) => res.send("OK");
```

### Fix 4: Set up conditional exports in package.json

```json
{
  "name": "my-package",
  "type": "module",
  "exports": {
    ".": {
      "import": "./src/index.js",
      "require": "./src/index.cjs"
    },
    "./utils": "./src/utils.js"
  }
}
```

```javascript
// Consumers can then import subpaths
import { helper } from "my-package/utils";
```

### Fix 5: Debug module resolution

```bash
# Enable ESM resolution debugging
NODE_OPTIONS="--experimental-specifier-resolution=node" node --input-type=module \
  -e 'import { createRequire } from "module"; console.log("ok")'

# List all installed packages
ls node_modules/

# Check if a package has proper package.json
cat node_modules/my-package/package.json | grep -A5 '"exports"'
```

## Examples

```javascript
// Minimal ESM setup that avoids ERR_MODULE_NOT_FOUND

// package.json
// { "type": "module" }

// src/index.js
import { readConfig } from "./config.js";    // explicit extension
import { connect } from "./db/connection.js"; // full relative path
import express from "express";                // installed in node_modules

const config = readConfig();
const db = await connect(config.dbUrl);
```

## Related Errors

- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — cannot require an ES module from CJS.
- [MODULE_NOT_FOUND]({{< relref "/languages/javascript/modulenotfounderror" >}}) — CommonJS module not found.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/ERR_MODULE_NOT_FOUND" >}}) — detailed ESM resolution with package.json.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — module has syntax errors.
