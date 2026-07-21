---
title: "[Solution] Deprecated Function Migration: Array.prototype.slice.call to Array.from"
description: "Migrate from deprecated Array.prototype.slice.call to Array.from for converting array-like objects."
deprecated_function: "Array.prototype.slice.call(arrayLike)"
replacement_function: "Array.from(arrayLike)"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: Array.prototype.slice.call to Array.from

The `Array.prototype.slice.call(arrayLike)` has been deprecated in favor of `Array.from(arrayLike)`.

## Migration Guide

Array.from() is the modern, explicit way to create arrays from iterables and array-like objects.

## Before (Deprecated)

```javascript
var divs = document.querySelectorAll("div");
var divArray = Array.prototype.slice.call(divs);

var args = (function() { return arguments; })();
var argsArray = Array.prototype.slice.call(args);
```

## After (Modern)

```javascript
const divs = document.querySelectorAll("div");
const divArray = Array.from(divs);

const argsArray = Array.from(arguments);

// With mapping
const doubled = Array.from([1, 2, 3], x => x * 2);
```

## Key Differences

- Array.from converts array-like and iterables
- Supports a mapping function
- More readable than slice.call
