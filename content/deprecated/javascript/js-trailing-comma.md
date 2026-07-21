---
title: "[Solution] Deprecated Function Migration: avoiding trailing commas to ES5+"
description: "Migrate from deprecated pattern of avoiding trailing commas."
deprecated_function: "No trailing commas"
replacement_function: "Trailing commas"
languages: ["javascript"]
deprecated_since: "ES5+"
---

# [Solution] Deprecated Function Migration: avoiding trailing commas to ES5+

The `No trailing commas` has been deprecated in favor of `Trailing commas`.

## Migration Guide

Trailing commas simplify git diffs

Trailing commas were avoided in ES3. ES5+ supports them.

## Before (Deprecated)

```javascript
const obj = {
    a: 1,
    b: 2
}
```

## After (Modern)

```javascript
const obj = {
    a: 1,
    b: 2,
}
```

## Key Differences

- Trailing commas simplify diffs
- Standard in ES5+
- ESLint enforces trailing commas
