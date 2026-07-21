---
title: "[Solution] Deprecated Function Migration: arguments object to rest parameters"
description: "Migrate from deprecated arguments object to rest parameters in JavaScript for cleaner variadic functions."
deprecated_function: "arguments object"
replacement_function: "...rest parameters"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: arguments object to rest parameters

The `arguments object` has been deprecated in favor of `...rest parameters`.

## Migration Guide

Rest parameters (...args) create a real array and work with arrow functions, unlike the arguments object.

## Before (Deprecated)

```javascript
function sum() {
    var total = 0;
    for (var i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}
```

## After (Modern)

```javascript
function sum(...numbers) {
    return numbers.reduce((total, n) => total + n, 0);
}

// Arrow functions can use rest params
const log = (...args) => console.log(...args);
```

## Key Differences

- ...args creates a real Array
- Works with arrow functions
- More explicit function signature
