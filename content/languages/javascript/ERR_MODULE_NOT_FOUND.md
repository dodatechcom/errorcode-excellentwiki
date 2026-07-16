---
title: "[Solution] Node.js ERR_MODULE_NOT_FOUND — Module Not Found Fix"
description: "Fix Node.js ERR_MODULE_NOT_FOUND by checking package.json exports, file extensions in imports, type: module, and import resolution."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
tags: ["err-module-not-found", "esm", "commonjs", "package.json", "nodejs"]
weight: 82
---

# Node.js ERR_MODULE_NOT_FOUND — Module Not Found Fix

The `ERR_MODULE_NOT_FOUND` error in Node.js occurs when the ESM (ECmascript Module) loader cannot resolve an import path. Unlike CommonJS `require()`, ESM `import` requires explicit file extensions, does not resolve directories, and is affected by the `exports` field in `package.json`. This error is common when migrating from CommonJS to ESM.

## Common Causes

```javascript
// Cause 1: Missing file extension in relative imports
// File: app.mjs
import { helper } from "./utils";  // ERR_MODULE_NOT_FOUND (should be "./utils.js")

// Cause 2: Directory import without index file
import { db } from "./models";  // ERR_MODULE_NOT_FOUND (no ./models/index.js)

// Cause 3: Package without "type": "module" in package.json
// package.json has no "type" field, but file uses .js extension with import syntax
import express from "express";  // ERR_MODULE_NOT_FOUND

// Cause 4: Missing package or typo
import lodash from "lodsh";  // ERR_MODULE_NOT_FOUND

// Cause 5: Package.json "exports" field blocks the import path
import helper from "my-package/src/helper.js";  // ERR_PACKAGE_PATH_NOT_EXPORTED
```

## Solutions

### Fix 1: Add file extensions to relative imports

```javascript
// Wrong — ESM requires explicit extensions
import { helper } from "./utils";
import { db } from "./models/connection";

// Correct — include the file extension
import { helper } from "./utils.js";
import { db } from "./models/connection.js";
```

### Fix 2: Configure package.json for ESM

```json
{
  "name": "my-app",
  "type": "module",
  "main": "./src/index.js"
}
```

Without `"type": "module"`, Node.js treats `.js` files as CommonJS. You can also use `.mjs` extensions to force ESM regardless of the `type` field:

```javascript
// app.mjs — always treated as ESM regardless of package.json
import express from "express";
export const handler = (req, res) => res.send("OK");
```

### Fix 3: Use import maps or full paths instead of directory imports

```javascript
// Wrong — directory import (not supported in ESM)
import { User } from "./models";
import { Router } from "./routes";

// Correct — import the specific file
import { User } from "./models/user.js";
import { Router } from "./routes/index.js";

// Or use a package.json "exports" map in the package itself
```

### Fix 4: Use conditional exports in package.json

```json
{
  "name": "my-package",
  "type": "module",
  "exports": {
    ".": {
      "import": "./src/index.js",
      "require": "./src/index.cjs"
    },
    "./utils": "./src/utils.js",
    "./models/*": "./src/models/*.js"
  }
}
```

Now consumers can import:

```javascript
import { helper } from "my-package/utils";
import { User } from "my-package/models/user.js";
```

### Fix 5: Dual CJS/ESM package setup

```javascript
// src/index.mjs — ESM entry point
export { processData } from "./processor.mjs";
```

```javascript
// src/index.cjs — CommonJS entry point
module.exports = {
    processData: require("./processor.cjs").processData,
};
```

```json
{
  "type": "module",
  "exports": {
    ".": {
      "import": "./src/index.mjs",
      "require": "./src/index.cjs"
    }
  },
  "main": "./src/index.cjs"
}
```

### Fix 6: Debug module resolution

```bash
# Check which files Node.js resolves for an import
node --experimental-specifier-resolution=node --input-type=module \
  -e 'import { createRequire } from "module"; console.log(import.meta.url)';

# Enable debug logging for module resolution
NODE_OPTIONS="--experimental-loader ./loader.mjs" node app.mjs

# Check if the module exists at all
ls -la node_modules/my-module/package.json
```

## Quick Checklist

| Issue | Fix |
|---|---|
| Missing file extension | Add `.js` to all relative imports |
| No `"type": "module"` | Add `"type": "module"` to package.json |
| Directory imports | Import specific file (e.g., `./models/user.js`) |
| Package not installed | Run `npm install` |
| Package blocks subpath | Check the package's `exports` field |
| Mixing CJS and ESM | Use conditional exports or `.mjs`/`.cjs` extensions |

## Prevention Tips

- Always use explicit file extensions (`.js`, `.mjs`) in ESM imports.
- Set `"type": "module"` in package.json when using `import`/`export` syntax.
- Use TypeScript with `"moduleResolution": "node16"` or `"bundler"` to catch missing extensions at compile time.
- Test both ESM and CommonJS entry points when publishing packages.

## Related Errors

- [ERR_SOCKET_TIMEOUT](ERR_SOCKET_TIMEOUT) — Node.js network timeout error.
- [TypeError](typeerror) — value is not the expected type.
- [ReferenceError](referenceerror) — variable not defined in scope.
