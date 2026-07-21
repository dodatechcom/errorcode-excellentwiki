---
title: "[Solution] Deprecated Function Migration: charAt() to at()"
description: "Migrate from deprecated String.charAt() to String.at() for character access in JavaScript."
deprecated_function: "str.charAt(index)"
replacement_function: "str.at(index)"
languages: ["javascript"]
deprecated_since: "ES2022"
---

# [Solution] Deprecated Function Migration: charAt() to at()

The `str.charAt(index)` has been deprecated in favor of `str.at(index)`.

## Migration Guide

at() supports negative indexing and is more modern.

## Before (Deprecated)

```javascript
const str = "Hello";
const char = str.charAt(0);
const last = str.charAt(str.length - 1);
```

## After (Modern)

```javascript
const str = "Hello";
const char = str.at(0);
const last = str.at(-1);  // Negative indexing

// Also works on arrays
const arr = [1, 2, 3];
const first = arr.at(0);
const lastArr = arr.at(-1);
```

## Key Differences

- at() supports negative indexing
- Works on both strings and arrays
- More modern and readable
