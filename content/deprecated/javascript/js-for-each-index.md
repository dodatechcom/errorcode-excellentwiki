---
title: "[Solution] Deprecated Function Migration: forEach with index to for...of with entries"
description: "Migrate from deprecated forEach for index to for...of with entries."
deprecated_function: "arr.forEach((item, index) => { })"
replacement_function: "for (const [index, item] of arr.entries()) { }"
languages: ["javascript"]
deprecated_since: "ES2015+"
---

# [Solution] Deprecated Function Migration: forEach with index to for...of with entries

The `arr.forEach((item, index) => { })` has been deprecated in favor of `for (const [index, item] of arr.entries()) { }`.

## Migration Guide

for...of with entries is more flexible.

## Before (Deprecated)

```javascript
arr.forEach((item, index) => {
    console.log(index, item);
});
```

## After (Modern)

```javascript
for (const [index, item] of arr.entries()) {
    console.log(index, item);
}
```

## Key Differences

- for...of with entries is more flexible
