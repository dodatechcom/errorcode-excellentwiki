---
title: "[Solution] Deprecated Function Migration: arguments.length to rest parameters"
description: "Migrate from deprecated arguments.length checks to rest parameters."
deprecated_function: "arguments.length"
replacement_function: "...args.length"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: arguments.length to rest parameters

The `arguments.length` has been deprecated in favor of `...args.length`.

## Migration Guide

Rest parameters create a proper array

arguments is array-like. Rest parameters provide a real array.

## Before (Deprecated)

```javascript
function sum() {
    if (arguments.length === 0) return 0;
}
```

## After (Modern)

```javascript
function sum(...args) {
    if (args.length === 0) return 0;
    return args.reduce((t, n) => t + n, 0);
}
```

## Key Differences

- Rest parameters are real arrays
- arguments is array-like only
- Works with arrow functions
