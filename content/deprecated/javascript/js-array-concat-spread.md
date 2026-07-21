---
title: "[Solution] Deprecated Function Migration: arr.concat to spread operator"
description: "Migrate from deprecated concat to spread operator."
deprecated_function: "arr1.concat(arr2)"
replacement_function: "[...arr1, ...arr2]"
languages: ["javascript"]
deprecated_since: "ES2015"
---

# [Solution] Deprecated Function Migration: arr.concat to spread operator

The `arr1.concat(arr2)` has been deprecated in favor of `[...arr1, ...arr2]`.

## Migration Guide

Spread is more concise.

## Before (Deprecated)

```javascript
const combined = arr1.concat(arr2);
```

## After (Modern)

```javascript
const combined = [...arr1, ...arr2];
```

## Key Differences

- Spread is more concise
