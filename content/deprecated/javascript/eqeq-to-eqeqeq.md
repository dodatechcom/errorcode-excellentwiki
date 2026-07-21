---
title: "[Solution] Deprecated Function Migration: == to === strict equality"
description: "Migrate from deprecated loose equality == to strict equality === in JavaScript."
deprecated_function: "== / !="
replacement_function: "=== / !=="
languages: ["javascript"]
deprecated_since: "ES5.1+"
---

# [Solution] Deprecated Function Migration: == to === strict equality

The `== / !=` has been deprecated in favor of `=== / !==`.

## Migration Guide

Loose equality (==) performs type coercion leading to unexpected results. Strict equality (===) compares both value and type.

## Before (Deprecated)

```javascript
0 == ""        // true
null == undefined  // true
"0" == false  // true
[] == false   // true
```

## After (Modern)

```javascript
0 === ""        // false
null === undefined  // false
"0" === false  // false
[] === false   // false

// Use null/undefined checks explicitly
value === null || value === undefined
```

## Key Differences

- Always use === and !== instead of == and !=
- value == null is the one exception
- Enable ESLint eqeqeq rule
