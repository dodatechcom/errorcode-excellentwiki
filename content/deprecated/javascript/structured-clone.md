---
title: "[Solution] Deprecated Function Migration: JSON.parse(JSON.stringify()) to structuredClone"
description: "Migrate from deprecated JSON deep copy pattern to structuredClone in JavaScript."
deprecated_function: "JSON.parse(JSON.stringify(obj))"
replacement_function: "structuredClone(obj)"
languages: ["javascript"]
deprecated_since: "ES2022"
---

# [Solution] Deprecated Function Migration: JSON.parse(JSON.stringify()) to structuredClone

The `JSON.parse(JSON.stringify(obj))` has been deprecated in favor of `structuredClone(obj)`.

## Migration Guide

structuredClone handles more types (Date, RegExp, Map, Set) and avoids JSON serialization issues.

## Before (Deprecated)

```javascript
const copy = JSON.parse(JSON.stringify(original));
// Problems: loses Date, RegExp, undefined, functions,
// circular references cause errors
```

## After (Modern)

```javascript
const copy = structuredClone(original);
// Supports: Date, RegExp, Map, Set, ArrayBuffer,
// circular references, and more types
```

## Key Differences

- structuredClone handles more data types
- Supports circular references
- No JSON serialization overhead
- Does not handle functions
