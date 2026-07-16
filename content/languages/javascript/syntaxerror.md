---
title: "[Solution] JavaScript SyntaxError — Unexpected Token Fix"
description: "Fix JavaScript SyntaxError: unexpected token. Find and fix syntax issues like missing brackets, trailing commas, invalid characters, and import errors."
languages: ["javascript"]
severities: ["error"]
error_types: ["syntax"]
tags: ["syntaxerror", "syntax", "parse", "token"]
weight: 80
---

# SyntaxError — Unexpected Token Fix

A `SyntaxError` is thrown when the JavaScript parser encounters code that violates the language grammar. Unlike `ReferenceError` or `TypeError` which happen at runtime, `SyntaxError` occurs during the parsing phase before any code executes — meaning the entire script file fails to load.

## Description

Common SyntaxError messages include:

- `SyntaxError: Unexpected token ';'` — the parser did not expect a token at that position.
- `SyntaxError: Unexpected end of input` — unclosed bracket, parenthesis, or string.
- `SyntaxError: Invalid or unexpected token` — non-printable or invalid characters in code.
- `SyntaxError: Cannot use import statement outside a module` — using ES modules in a script tag.
- `SyntaxError: Unexpected token 'return'` — return statement outside of a function.

SyntaxError cannot be caught with try/catch because the code never begins executing.

## Common Causes

```javascript
// Cause 1: Missing closing bracket, parenthesis, or semicolon
function greet() {
    console.log("hello")
// Missing closing brace

// Cause 2: Trailing comma in older environments
const config = {
    host: "localhost",
    port: 3000,  // trailing comma fails in IE11 and some older Node versions
};

// Cause 3: Using async/await outside async function
async function fetchData() {
    const data = await fetch("/api");  // correct
}
fetchData();  // if fetchData is missing 'async', await is a SyntaxError

// Cause 4: Import/export in non-module context
<script>
    import { helper } from "./utils.js";  // SyntaxError in script context
</script>

// Cause 5: Invalid characters in code (zero-width spaces, smart quotes)
const name = "Alice";  // contains invisible Unicode characters
```

## Solutions

### Fix 1: Balance all brackets and parentheses

```javascript
// Wrong - missing closing parenthesis
if (true {
    console.log("yes");
}

// Correct
if (true) {
    console.log("yes");
}
```

```bash
# Use a linter to catch unclosed brackets automatically
npx eslint src/
```

### Fix 2: Remove or handle trailing commas for compatibility

```javascript
// Wrong for ES5 environments
const arr = [1, 2, 3,];

// Correct - no trailing comma for older targets
const arr = [1, 2, 3];

// For ES2017+ environments, trailing commas are valid and encouraged
const arr = [1, 2, 3,];  // valid in modern JS
```

### Fix 3: Ensure await is only used inside async functions

```javascript
// Wrong - await outside async function
async function fetchUser() {
    const response = await fetch("/api/user");
    return response.json();
}
// If this file is loaded as a non-module, "await" is a SyntaxError

// Correct - ensure the context supports top-level await
// Option A: wrap in async IIFE
(async () => {
    const response = await fetch("/api/user");
    const data = await response.json();
})();

// Option B: use .then() for non-async contexts
fetch("/api/user")
    .then(response => response.json())
    .then(data => console.log(data));
```

### Fix 4: Use type="module" for ES module syntax

```html
<!-- Wrong - import is a SyntaxError in regular script -->
<script>
    import { helper } from "./utils.js";
</script>

<!-- Correct - declare the script as a module -->
<script type="module">
    import { helper } from "./utils.js";
</script>
```

### Fix 5: Remove invisible Unicode characters

```javascript
// Wrong - may contain zero-width spaces or smart quotes
const message = "hello\u200Bworld";

// Correct - clean the source file
const message = "helloworld";
```

```bash
# Find invisible characters in a file
cat -A src/app.js | grep -n $'\xe2\x80\x8b'

# Use sed to remove zero-width spaces
sed -i 's/\xe2\x80\x8b//g' src/app.js
```

### Fix 6: Validate syntax before executing with a parser check

```bash
# Check syntax without executing
node --check src/app.js

# If the file has syntax errors, node outputs the error and exits non-zero
# No code is executed — purely a parse check
```

```javascript
// Use the Function constructor to validate syntax at runtime
function isValidSyntax(code) {
    try {
        new Function(code);
        return true;
    } catch (e) {
        return e instanceof SyntaxError;
    }
}

isValidSyntax("const x = 1;");   // true
isValidSyntax("const x = ;");    // false
```

## Prevention Tips

- Use ESLint with `parser-options.ecmaVersion` set to your target environment.
- Configure Prettier to auto-format and catch structural issues on save.
- Run `node --check` or `tsc --noEmit` as a pre-commit hook.
- Use TypeScript for static syntax and type checking before deployment.

## Related Errors

- [ReferenceError](referenceerror) — syntax is valid but a variable is not defined.
- [TypeError](typeerror) — syntax is valid but a value is the wrong type.
- [ImportError / ModuleNotFoundError](#) — module exists syntactically but cannot be located at runtime.
