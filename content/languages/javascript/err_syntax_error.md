---
title: "[Solution] Node.js ERR_SYNTAX_ERROR — Syntax Error in Node.js Fix"
description: "Fix Node.js ERR_SYNTAX_ERROR when evaluating code, parsing JSON, or loading modules with invalid syntax. Check file contents and parser compatibility."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-syntax-error", "syntax", "parse", "json", "eval", "nodejs"]
weight: 5
---

# Node.js ERR_SYNTAX_ERROR — Syntax Error in Node.js Fix

The `ERR_SYNTAX_ERROR` error in Node.js indicates that code could not be parsed or evaluated due to invalid syntax. This differs from the browser `SyntaxError` as it includes Node.js-specific contexts like `vm.compileFunction`, `eval`, `JSON.parse`, and module loading with unsupported syntax.

## Description

Common ERR_SYNTAX_ERROR messages include:

- `ERR_SYNTAX_ERROR: Cannot parse as JSON` — invalid JSON input.
- `ERR_SYNTAX_ERROR: Invalid syntax in module evaluation` — ESM/CJS syntax mismatch.
- `SyntaxError: Cannot use import statement outside a module` — using `import` in a non-module context.
- `SyntaxError: Unexpected token 'export'` — `export` in a CJS file.

## Common Causes

```javascript
// Cause 1: Invalid JSON
JSON.parse("{ name: 'Alice' }");  // SyntaxError: unexpected token

// Cause 2: Using ESM syntax in a CJS file
// file: app.js (no "type": "module" in package.json)
import express from "express";  // SyntaxError: Cannot use import statement

// Cause 3: Using CJS syntax in an ESM file
// file: app.mjs or package.json has "type": "module"
const express = require("express");  // ReferenceError: require is not defined

// Cause 4: eval() with invalid code
eval("function { broken }");  // SyntaxError
```

## Solutions

### Fix 1: Use JSON.parse with proper validation

```javascript
// Wrong — crashes on invalid JSON
const config = JSON.parse(userInput);

// Correct — validate first or catch the error
function safeJsonParse(str) {
  try {
    return { data: JSON.parse(str), error: null };
  } catch (err) {
    return { data: null, error: err.message };
  }
}

const { data, error } = safeJsonParse('{"key": "value"}');
if (error) {
  console.error("Invalid JSON:", error);
}
```

### Fix 2: Match file extension to module system

```json
{
  "name": "my-app",
  "type": "module"
}
```

```javascript
// With "type": "module" — use import/export
import express from "express";
export default function handler() {}

// Without "type": "module" — use require/module.exports
const express = require("express");
module.exports = function handler() {};
```

### Fix 3: Validate syntax before evaluation

```bash
# Check syntax without executing
node --check src/app.js

# Check a module
node --input-type=module --check < /dev/null
```

```javascript
// Validate code at runtime (CJS)
function isValidSyntax(code) {
  try {
    new Function(code);
    return true;
  } catch (err) {
    return err instanceof SyntaxError;
  }
}

isValidSyntax("const x = 1;");   // true
isValidSyntax("const x = ;");    // false
```

### Fix 4: Use vm module for sandboxed evaluation

```javascript
const vm = require("vm");

const context = { result: 0 };
try {
  vm.createContext(context);
  vm.runInContext("result = 2 + 2", context);
  console.log(context.result);  // 4
} catch (err) {
  if (err instanceof SyntaxError) {
    console.error("Invalid syntax in evaluated code");
  } else {
    throw err;
  }
}
```

## Examples

```javascript
// ERR_SYNTAX_ERROR with template literals in non-ESM
// file: script.js (no "type": "module")
eval("`Hello ${name}`");  // works — template literals are valid in all modern JS

// ERR_SYNTAX_ERROR with import.meta in CJS
console.log(import.meta.url);  // SyntaxError: Cannot use 'import.meta' outside a module

// ERR_SYNTAX_ERROR with top-level await in CJS
await fetch("/api");  // SyntaxError: await is only valid in async functions
```

## Related Errors

- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — browser-level syntax error.
- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — cannot require an ES module.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err_module_not_found" >}}) — ESM import resolution failed.
- [DataError]({{< relref "/languages/javascript/enodata" >}}) — data is invalid or malformed.
