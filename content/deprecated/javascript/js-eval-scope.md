---
title: "[Solution] Deprecated Function Migration: eval() for scope to let/const"
description: "Migrate from deprecated eval() scope to let/const block scoping."
deprecated_function: "eval() with local scope"
replacement_function: "let x = 1"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: eval() for scope to let/const

The `eval("var x = 1")` has been deprecated in favor of `let x = 1`.

## Migration Guide

let/const provide block scope without eval

eval can create variables in scope. let/const provide proper scoping.

## Before (Deprecated)

```javascript
eval("var x = 1");
```

## After (Modern)

```javascript
let x = 1;  // block scoped
for (let i = 0; i < 3; i++) { }
```

## Key Differences

- let/const provide block scope
- No need for eval
- eval is a security risk
