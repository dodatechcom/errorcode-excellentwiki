---
title: "[Solution] Deprecated Function Migration: String split for single delimiter to includes/indexOf"
description: "Migrate from deprecated String split pattern for membership testing to includes."
deprecated_function: "str.split(',').includes(x)"
replacement_function: "str.includes(x)"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: String split for single delimiter to includes/indexOf

The `str.split(',').includes(x)` has been deprecated in favor of `str.includes(x)`.

## Migration Guide

split+includes is wasteful; includes checks directly

Using split to check membership creates an unnecessary array.

## Before (Deprecated)

```javascript
const csv = "apple,banana,cherry";
const hasBanana = csv.split(',').includes('banana');  // creates array
```

## After (Modern)

```javascript
const csv = "apple,banana,cherry";
const hasBanana = csv.includes('banana');  // direct check
```

## Key Differences

- includes checks directly without creating array
- More memory efficient
- Faster for simple membership checks
