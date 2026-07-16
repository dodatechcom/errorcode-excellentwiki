---
title: "[Solution] JavaScript var Deprecated — Use let/const for Block Scope"
description: "Replace deprecated var with let/const in JavaScript. Block scope, hoisting differences, best practices, and migration guide with code examples."
deprecated_function: "var"
replacement_function: "let/const"
languages: ["javascript"]
deprecated_since: "ES6"
error_message: "Consider using let or const instead of var"
tags: ["var", "let", "const", "block-scope", "hoisting", "es6"]
weight: 95
---

# [Solution] JavaScript var Deprecated — Use let/const for Block Scope

While `var` is not technically removed from JavaScript, it is widely considered deprecated in modern codebases. The `let` and `const` declarations (introduced in ES6/2015) provide block scoping, prevent hoisting-related bugs, and make code behavior more predictable. Major linters (ESLint `no-var` rule), style guides, and TypeScript all recommend replacing `var` with `let` or `const`.

## Why var is Problematic

```javascript
// Problem 1: Function scope instead of block scope
for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100);
}
// Prints: 3, 3, 3 (not 0, 1, 2 — var is function-scoped)

// Problem 2: Hoisting leads to unexpected undefined
console.log(x);  // undefined (not a ReferenceError!)
var x = 5;

// Problem 3: Re-declaration is allowed (silent bug)
var count = 1;
var count = 2;  // no error — easy to make mistakes

// Problem 4: Global pollution
function example() {
    var global = "oops";  // leaks to window.global
}
console.log(window.global);  // "oops"
```

## Old Code (var)

```javascript
// var in loops — classic closure bug
var buttons = document.querySelectorAll("button");
for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function() {
        console.log("Button " + i);  // always prints the last value of i
    });
}

// var hoisting
console.log(name);  // undefined (no error!)
var name = "Alice";

// var re-declaration
var x = 1;
var x = 2;  // silent — no error

// var in if blocks — leaks out
if (true) {
    var temp = 42;
}
console.log(temp);  // 42 — leaked out of the if block
```

## New Code (let/const)

```javascript
// let in loops — correct closure behavior
const buttons = document.querySelectorAll("button");
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function() {
        console.log("Button " + i);  // prints correct index
    });
}

// let — no hoisting surprise
// console.log(name);  // ReferenceError: Cannot access 'name' before initialization
let name = "Alice";

// const — cannot re-declare or reassign
const x = 1;
// x = 2;  // TypeError: Assignment to constant variable
// const x = 3;  // SyntaxError: Identifier 'x' has already been declared

// let in if blocks — properly scoped
if (true) {
    let temp = 42;
}
// console.log(temp);  // ReferenceError: temp is not defined
```

## Rules of Thumb

```javascript
// Rule 1: Use const by default — the value never changes
const API_URL = "https://api.example.com";
const config = { timeout: 5000 };
const users = ["Alice", "Bob"];

// Rule 2: Use let when the value needs to change
let counter = 0;
let currentUser = null;

// Rule 3: Never use var in new code
// var x = 5;  // DON'T DO THIS

// Rule 4: Destructuring with const/let
const { name, age } = user;
let [first, ...rest] = items;

// Rule 5: for...of with const for loop body
const items = [1, 2, 3];
for (const item of items) {
    console.log(item);  // each iteration gets a new binding
}

// Rule 6: for with index uses let
for (let i = 0; i < items.length; i++) {
    console.log(i, items[i]);
}
```

## var vs let vs const Comparison

| Feature | `var` | `let` | `const` |
|---|---|---|---|
| Scope | Function | Block | Block |
| Hoisting | Yes (initialized as `undefined`) | Yes (TDZ) | Yes (TDZ) |
| Re-declaration | Allowed | Not allowed | Not allowed |
| Reassignment | Allowed | Allowed | Not allowed |
| Global object property | Yes (`window.x`) | No | No |
| Temporal Dead Zone | No | Yes | Yes |

TDZ = Temporal Dead Zone — accessing the variable before its declaration throws a `ReferenceError`.

## Migration Steps

1. **Enable ESLint `no-var` rule**:

```json
{
  "rules": {
    "no-var": "error",
    "prefer-const": "error",
    "prefer-let": "warn"
  }
}
```

2. **Find all var declarations**:

```bash
grep -rn "\bvar " --include="*.js" --include="*.ts" /path/to/project/
```

3. **Replace `var` with `const`** for variables that are never reassigned.

4. **Replace `var` with `let`** for variables that are reassigned.

5. **Verify there are no re-declarations** — `var` allows them but `let`/`const` do not.

6. **Watch for hoisting changes** — `var` is hoisted and initialized as `undefined`; `let`/`const` are hoisted but not initialized (TDZ).

7. **Run your test suite** to catch any behavioral changes from the scoping differences.

## Migration Using Code Mods

Facebook's `js-codemod` automates much of this:

```bash
npx jscodeshift --extensions=js,jsx -t jscodeshift/transforms/no-vars.js /path/to/project/
```

## Related Errors

- [RangeError](rangeerror) — value outside valid range.
- [TypeError](typeerror) — value is not the expected type.
- [escape()/unescape() deprecated](escape-unescape) — another deprecated JavaScript feature.
