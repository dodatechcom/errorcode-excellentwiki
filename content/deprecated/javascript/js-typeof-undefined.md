---
title: "[Solution] Deprecated Function Migration: typeof x === undefined to x === undefined"
description: "Migrate from deprecated typeof undefined check to direct comparison."
deprecated_function: "typeof x === 'undefined'"
replacement_function: "x === undefined"
languages: ["javascript"]
deprecated_since: "ES5+"
---

# [Solution] Deprecated Function Migration: typeof x === undefined to x === undefined

The `typeof x === 'undefined'` has been deprecated in favor of `x === undefined`.

## Migration Guide

Direct comparison is cleaner.

## Before (Deprecated)

```javascript
if (typeof x === 'undefined') { }
```

## After (Modern)

```javascript
if (x === undefined) { }
```

## Key Differences

- Direct comparison is cleaner
