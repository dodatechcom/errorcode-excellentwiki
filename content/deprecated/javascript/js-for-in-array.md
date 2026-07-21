---
title: "[Solution] Deprecated Function Migration: for...in with arrays to for...of"
description: "Migrate from deprecated for...in with arrays to for...of."
deprecated_function: "for (var key in arr)"
replacement_function: "for (const item of arr)"
languages: ["javascript"]
deprecated_since: "ES2015"
---

# [Solution] Deprecated Function Migration: for...in with arrays to for...of

The `for (var key in arr)` has been deprecated in favor of `for (const item of arr)`.

## Migration Guide

for...of gives values. for...in gives keys.

## Before (Deprecated)

```javascript
for (var key in arr) {
    console.log(arr[key]);
}
```

## After (Modern)

```javascript
for (const item of arr) {
    console.log(item);
}
```

## Key Differences

- for...of gives values directly
