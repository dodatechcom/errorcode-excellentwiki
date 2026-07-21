---
title: "[Solution] Deprecated Function Migration: bracket notation with length-1 to at()"
description: "Migrate from deprecated arr[arr.length - 1] to arr.at(-1) for last element access."
deprecated_function: "arr[arr.length - 1]"
replacement_function: "arr.at(-1)"
languages: ["javascript"]
deprecated_since: "ES2022"
---

# [Solution] Deprecated Function Migration: bracket notation with length-1 to at()

The `arr[arr.length - 1]` has been deprecated in favor of `arr.at(-1)`.

## Migration Guide

at() with negative indices provides a cleaner way to access elements from the end.

## Before (Deprecated)

```javascript
const arr = [1, 2, 3, 4, 5];
const last = arr[arr.length - 1];
const secondLast = arr[arr.length - 2];
```

## After (Modern)

```javascript
const arr = [1, 2, 3, 4, 5];
const last = arr.at(-1);
const secondLast = arr.at(-2);
const first = arr.at(0);
```

## Key Differences

- at() supports negative indexing
- More concise than arr[arr.length - 1]
- Works on strings too
