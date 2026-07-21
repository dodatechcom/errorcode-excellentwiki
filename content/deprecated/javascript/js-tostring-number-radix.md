---
title: "[Solution] Deprecated Function Migration: Number(radix) to parseInt with explicit radix"
description: "Migrate from deprecated parseInt without radix to parseInt with explicit radix."
deprecated_function: "parseInt(str)"
replacement_function: "parseInt(str, 10)"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: Number(radix) to parseInt with explicit radix

The `parseInt(str)` has been deprecated in favor of `parseInt(str, 10)`.

## Migration Guide

Always specify radix to avoid unexpected octal parsing

parseInt without radix can parse strings starting with 0 as octal in older engines.

## Before (Deprecated)

```javascript
# Deprecated -- radix not specified
parseInt("010")  // might be 8 (octal) or 10

# Also deprecated
parseInt("0x10")  // 16 (hex) but implicit
```

## After (Modern)

```javascript
# Always specify radix
parseInt("010", 10)  // 10
parseInt("0x10", 16)  // 16
parseInt("101", 2)   // 5

# Modern alternative for hex
Number("0x10")  // 16
```

## Key Differences

- Always specify radix parameter
- 10 for decimal, 16 for hex, 2 for binary
- Number() for automatic base detection
- parseInt with radix is safer
