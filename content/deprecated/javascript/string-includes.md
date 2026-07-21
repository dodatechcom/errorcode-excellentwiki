---
title: "[Solution] Deprecated Function Migration: indexOf to includes"
description: "Migrate from deprecated indexOf checks to includes() for string and array membership in JavaScript."
deprecated_function: "str.indexOf(x) !== -1"
replacement_function: "str.includes(x)"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: indexOf to includes

The `str.indexOf(x) !== -1` has been deprecated in favor of `str.includes(x)`.

## Migration Guide

includes() returns a boolean directly and reads like natural English, replacing verbose indexOf checks.

## Before (Deprecated)

```javascript
var str = "Hello, World!";
if (str.indexOf("World") !== -1) {
    console.log("Found");
}

var arr = [1, 2, 3];
if (arr.indexOf(2) !== -1) {
    console.log("Found");
}
```

## After (Modern)

```javascript
const str = "Hello, World!";
if (str.includes("World")) {
    console.log("Found");
}

const arr = [1, 2, 3];
if (arr.includes(2)) {
    console.log("Found");
}
```

## Key Differences

- includes() returns true/false directly
- indexOf() returns -1 or the index
- includes() also works on arrays
