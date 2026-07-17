---
title: "[Solution] Node.js MODULE_NOT_FOUND — Module Not Found Fix"
description: "Fix Node.js MODULE_NOT_FOUND error by checking require paths, node_modules, package.json main field, and module resolution."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js MODULE_NOT_FOUND — Module Not Found Fix

The `MODULE_NOT_FOUND` error in Node.js occurs when a `require()` call cannot locate the specified module. This is the CommonJS equivalent of `ERR_MODULE_NOT_FOUND` and typically indicates a missing file, incorrect path, or incomplete `node_modules` installation.

## Description

Common MODULE_NOT_FOUND messages include:

- `Error: Cannot find module './utils'` — relative path resolution failed.
- `Error: Cannot find module 'express'` — package not installed in `node_modules`.
- `Error: Cannot find module './config' from '/app/src'` — path resolution starts from the wrong directory.

## Common Causes

```javascript
// Cause 1: Missing file extension or wrong extension
const utils = require("./utils");    // fails if file is utils.mjs
const utils = require("./utils.js"); // correct

// Cause 2: Package not installed
const lodash = require("lodash");  // MODULE_NOT_FOUND if not in node_modules

// Cause 3: Typo in module path
const config = require("./confige");  // MODULE_NOT_FOUND — typo

// Cause 4: Circular dependency that breaks resolution
// a.js requires b.js, b.js requires a.js — may produce MODULE_NOT_FOUND

// Cause 5: Module installed but package.json "main" points to missing file
const pkg = require("some-package");  // MODULE_NOT_FOUND if main is wrong
```

## Solutions

### Fix 1: Verify the file exists at the expected path

```javascript
const path = require("path");
const fs = require("fs");

function safeRequire(modulePath) {
  const resolved = require.resolve(modulePath);
  if (!fs.existsSync(resolved)) {
    console.error("Module resolved to non-existent file:", resolved);
    return null;
  }
  return require(modulePath);
}

const utils = safeRequire("./utils");
```

### Fix 2: Install missing dependencies

```bash
# Check if a package is installed
ls node_modules/express

# Reinstall node_modules if many modules are missing
rm -rf node_modules package-lock.json
npm install

# For yarn
yarn install

# For pnpm
pnpm install
```

### Fix 3: Use require.resolve to debug resolution

```javascript
// Find where Node.js resolves a module
try {
  const resolvedPath = require.resolve("lodash");
  console.log("Resolved to:", resolvedPath);
} catch (err) {
  console.error("Module not found:", err.message);
  // Shows the exact path Node.js tried to load
}

// Check custom paths
try {
  const customPath = require.resolve("./src/config/database");
  console.log("Database config at:", customPath);
} catch (err) {
  console.error("Could not find database config module");
}
```

### Fix 4: Handle circular dependencies

```javascript
// a.js
const b = require("./b");
module.exports = { fromA: () => `A calls ${b.fromB()}` };

// b.js
const a = require("./a");  // may get incomplete exports
module.exports = { fromB: () => `B calls ${a.fromA?.() ?? "undefined"}` };

// Fix: lazy-load circular dependencies
// b.js
let a;
module.exports = {
  fromB: () => {
    a = a || require("./a");  // load on first use
    return `B calls ${a.fromA()}`;
  },
};
```

### Fix 5: Set NODE_PATH for absolute module lookups

```bash
# Set NODE_PATH to include additional directories
export NODE_PATH=/usr/local/lib/node_modules
node app.js
```

```javascript
// Or set it programmatically
module.paths.push("/opt/shared-modules");
const shared = require("shared-library");
```

## Examples

```javascript
// Debugging MODULE_NOT_FOUND step by step
console.log("Module paths:", module.paths);  // shows search directories

try {
  const db = require("./database/connection");
} catch (err) {
  console.error("Code:", err.code);           // MODULE_NOT_FOUND
  console.error("Message:", err.message);
  console.error("Required at:", err.stack.split("\n")[1]);
}
```

## Related Errors

- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — cannot require an ES module.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err_module_not_found" >}}) — ESM import resolution failed.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/ERR_MODULE_NOT_FOUND" >}}) — ESM resolution with package.json.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — module exists but has syntax errors.
