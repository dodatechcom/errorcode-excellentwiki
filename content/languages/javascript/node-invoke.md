---
title: "Node.js TypeError: X is not a function"
description: "TypeError: X is not a function — Fix Node.js function invocation errors."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nodejs", "typeerror", "not-a-function", "invoke", "undefined-function"]
weight: 5
---

The `TypeError: X is not a function` error occurs when you attempt to call something that is not a function. This is a runtime TypeError in Node.js, often caused by incorrect imports, wrong module usage, or calling methods on wrong types.

## Description

Common TypeError messages include:

- `TypeError: X is not a function` — X is undefined, null, or not a callable
- `TypeError: X(...).Y is not a function` — Y does not exist on the return value
- `TypeError: Cannot read properties of undefined (reading 'call')` — calling undefined as function

## Common Causes

```javascript
// Cause 1: Wrong import — default vs named export
import MyModule from "my-package"; // should be: import { MyModule } from "my-package"

// Cause 2: Module returns an object, not a function
const moment = require("moment"); // moment is a function
const config = require("./config"); // config is an object, not callable
config(); // TypeError: config is not a function

// Cause 3: Calling a method that does not exist
const arr = [1, 2, 3];
arr.find(); // TypeError: cannot read properties of undefined

// Cause 4: Wrong version of a package
// API changed between versions — old method removed
```

## Solutions

### Fix 1: Check the import style

```javascript
// If the module uses named exports
// Bad
const express = require("express");
const { Router } = express();
// Better: check the actual exports
const express = require("express");
console.log(typeof express); // function
console.log(Object.keys(express)); // check available properties

// If using ESM
import express from "express"; // default export
import { Router } from "express"; // named export
```

### Fix 2: Validate before calling

```javascript
function safeCall(fn, ...args) {
  if (typeof fn !== "function") {
    throw new TypeError(`${fn} is not a function`);
  }
  return fn(...args);
}

// Or check a module export before using
const myModule = require("./my-module");
if (typeof myModule.process === "function") {
  myModule.process(data);
} else {
  console.error("process is not a function:", typeof myModule.process);
}
```

### Fix 3: Verify package version compatibility

```bash
# Check installed version
npm list my-package

# Check if the API changed
npm info my-package versions

# Install a compatible version
npm install my-package@previous-version
```

## Examples

```javascript
// TypeError: express is not a function
// When express is imported incorrectly
const express = require("express");
// express is a function — this works

// TypeError: createError is not a function
// When importing from http-errors
const createError = require("http-errors");
// http-errors exports a function — this works

// TypeError when destructuring wrong
const { get } = require("lodash");
// lodash default export is an object — this fails
// Fix:
const _ = require("lodash");
_.get(obj, "path"); // works
```

## Related Errors

- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-cannot-find-module" >}}) — module not found.
- [ReferenceError]({{< relref "/languages/javascript/referenceerror" >}}) — variable not defined.
- [TypeError]({{< relref "/languages/javascript/typeerror" >}}) — general type error.
