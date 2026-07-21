---
title: "[Solution] Deprecated Function Migration: reduce+concat for flattening to flat()"
description: "Migrate from deprecated flatten patterns to Array.flat() and Array.flatMap() in JavaScript."
deprecated_function: "arr.reduce((a,b) => a.concat(b))"
replacement_function: "arr.flat()"
languages: ["javascript"]
deprecated_since: "ES2019"
---

# [Solution] Deprecated Function Migration: reduce+concat for flattening to flat()

The `arr.reduce((a,b) => a.concat(b))` has been deprecated in favor of `arr.flat()`.

## Migration Guide

flat() and flatMap() provide built-in array flattening without manual reduce/concat.

## Before (Deprecated)

```javascript
const nested = [[1, 2], [3, 4], [5]];
const flat = nested.reduce((acc, val) => acc.concat(val), []);

// With depth
const deep = [[1, [2]], [3, [4]]];
```

## After (Modern)

```javascript
const nested = [[1, 2], [3, 4], [5]];
const flat = nested.flat();

// With depth
const deep = [[1, [2]], [3, [4]]];
deep.flat(2);  // [1, 2, 3, 4]

// flatMap for map + flat
const result = [1, 2, 3].flatMap(x => [x, x * 2]);
```

## Key Differences

- flat() flattens by one level by default
- flat(n) for deeper nesting
- flatMap() combines map and flat
- More readable than reduce+concat
