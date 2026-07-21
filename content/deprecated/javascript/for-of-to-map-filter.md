---
title: "[Solution] Deprecated Function Migration: for loops to map/filter/reduce"
description: "Migrate from imperative for loops to functional array methods map/filter/reduce in JavaScript."
deprecated_function: "for loops for transformation"
replacement_function: "map/filter/reduce"
languages: ["javascript"]
deprecated_since: "ES5.1+"
---

# [Solution] Deprecated Function Migration: for loops to map/filter/reduce

The `for loops for transformation` has been deprecated in favor of `map/filter/reduce`.

## Migration Guide

map, filter, and reduce are declarative -- they express intent clearly and avoid off-by-one errors.

## Before (Deprecated)

```javascript
var numbers = [1, 2, 3, 4, 5];
var doubled = [];
var evens = [];
for (var i = 0; i < numbers.length; i++) {
    doubled.push(numbers[i] * 2);
    if (numbers[i] % 2 === 0) evens.push(numbers[i]);
}
```

## After (Modern)

```javascript
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((acc, n) => acc + n, 0);
```

## Key Differences

- map transforms each element
- filter selects elements matching a condition
- reduce accumulates elements into a single value
