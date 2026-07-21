---
title: "[Solution] Deprecated Function Migration: for...in to for...of for array iteration"
description: "Migrate from deprecated for...in array iteration to for...of in JavaScript."
deprecated_function: "for (var i in arr)"
replacement_function: "for (const item of arr)"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: for...in to for...of for array iteration

The `for (var i in arr)` has been deprecated in favor of `for (const item of arr)`.

## Migration Guide

for...in iterates over all enumerable properties including inherited ones. for...of iterates over values.

## Before (Deprecated)

```javascript
var arr = [10, 20, 30];
Array.prototype.custom = "oops";
for (var i in arr) {
    console.log(i);  // "0", "1", "2", "custom"
}
```

## After (Modern)

```javascript
const arr = [10, 20, 30];
for (const item of arr) {
    console.log(item);  // 10, 20, 30
}

// For index and value
for (const [index, value] of arr.entries()) {
    console.log(index, value);
}
```

## Key Differences

- for...of iterates values directly
- for...in iterates keys including prototype
- for...of works with any iterable
