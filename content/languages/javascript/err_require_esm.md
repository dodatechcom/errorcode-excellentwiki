---
title: "[Solution] Node.js ERR_REQUIRE_ESM — Cannot Require ES Module Fix"
description: "Fix Node.js ERR_REQUIRE_ESM by converting to dynamic import, using createRequire, or restructuring as CommonJS. Handle ESM-only packages."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_REQUIRE_ESM — Cannot Require ES Module Fix

The `ERR_REQUIRE_ESM` error occurs when a CommonJS module attempts to `require()` an ES module. Since ES modules use `import`/`export` syntax, they cannot be loaded synchronously via `require()`. This error is common when upgrading to Node.js 14+ where ESM-only packages become more prevalent.

## Description

Common ERR_REQUIRE_ESM messages include:

- `Error [ERR_REQUIRE_ESM]: require() of ES Module ... not supported` — direct require of ESM.
- `ERR_REQUIRE_ESM: Instead change the require of ... to a dynamic import()` — suggestion from Node.js.
- `ERR_REQUIRE_ESM: CommonJS module does not support ES module exports` — mixing module systems.

## Common Causes

```javascript
// Cause 1: require() an ESM-only package
const express = require("express");  // if express was published as ESM-only

// Cause 2: require() a local .mjs file
const utils = require("./utils.mjs");  // ERR_REQUIRE_ESM

// Cause 3: require() a package with "type": "module" in package.json
const myPkg = require("my-esm-package");  // ERR_REQUIRE_ESM

// Cause 4: CJS file in a package with "type": "module"
// package.json has "type": "module" but file uses require()
const data = require("./data");  // ERR_REQUIRE_ESM
```

## Solutions

### Fix 1: Use dynamic import() instead of require()

```javascript
// Wrong — ERR_REQUIRE_ESM
const myModule = require("esm-only-package");

// Correct — dynamic import() works in CommonJS
async function loadModule() {
  const myModule = await import("esm-only-package");
  return myModule.default;
}

loadModule().then((myModule) => {
  // use myModule
});
```

### Fix 2: Use createRequire to bridge CommonJS and ESM

```javascript
// When you need require() but are in an ESM context
import { createRequire } from "module";
const require = createRequire(import.meta.url);

const myModule = require("esm-only-package");
```

### Fix 3: Convert the calling file to ESM

```json
// package.json — change to ESM
{
  "name": "my-app",
  "type": "module"
}
```

```javascript
// app.mjs — now uses import instead of require
import myModule from "esm-only-package";
import { helper } from "./utils.mjs";

console.log(myModule, helper);
```

### Fix 4: Use conditional require with version checking

```javascript
async function loadPackage(name) {
  try {
    return require(name);
  } catch (err) {
    if (err.code === "ERR_REQUIRE_ESM") {
      console.log(`${name} is ESM-only, using dynamic import`);
      const mod = await import(name);
      return mod.default || mod;
    }
    throw err;
  }
}

// Usage
const pkg = await loadPackage("esm-only-package");
```

## Examples

```javascript
// Example: A CommonJS script needing an ESM-only dependency

// Before: ERR_REQUIRE_ESM
const yaml = require("yaml");
const config = yaml.parse(fs.readFileSync("config.yml", "utf-8"));

// After: dynamic import
async function loadConfig() {
  const yaml = await import("yaml");
  const content = fs.readFileSync("config.yml", "utf-8");
  return yaml.parse(content);
}

// Using top-level await (ESM only)
import yaml from "yaml";
const config = yaml.parse(fs.readFileSync("config.yml", "utf-8"));
```

## Related Errors

- [MODULE_NOT_FOUND]({{< relref "/languages/javascript/modulenotfounderror" >}}) — CommonJS module not found.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err_module_not_found" >}}) — ESM import resolution failed.
- [ERR_MISSING_ESM_TRANSPILER]({{< relref "/languages/javascript/err_missing_esm_transpiler" >}}) — missing transpiler for ESM.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/ERR_MODULE_NOT_FOUND" >}}) — detailed ESM resolution error.
