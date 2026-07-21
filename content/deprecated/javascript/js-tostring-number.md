---
title: "[Solution] Deprecated Function Migration: num.toString() to String(num)"
description: "Migrate from deprecated Number.toString patterns to String() for clarity."
deprecated_function: "num.toString()"
replacement_function: "String(num)"
languages: ["javascript"]
deprecated_since: "ES1+"
---

# [Solution] Deprecated Function Migration: num.toString() to String(num)

The `num.toString()` has been deprecated in favor of `String(num)`.

## Migration Guide

String() is more explicit for type conversion

Both work, but String() is more explicit about the intent of converting to string.

## Before (Deprecated)

```javascript
const num = 42;
const str1 = num.toString();
const str2 = (42).toString();  // parentheses needed
```

## After (Modern)

```javascript
const num = 42;
const str = String(num);

// For different bases
const bin = (42).toString(2);  // "101010"
const hex = (42).toString(16);  // "2a"
```

## Key Differences

- String() works without parentheses
- toString() requires parentheses for number literals
- String() is more explicit
- toString(radix) for base conversion
