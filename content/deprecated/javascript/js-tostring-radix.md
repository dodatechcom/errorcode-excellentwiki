---
title: "[Solution] Deprecated Function Migration: parseInt without radix to explicit radix"
description: "Migrate from deprecated parseInt without radix to parseInt with explicit radix."
deprecated_function: "parseInt(str)"
replacement_function: "parseInt(str, 10)"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: parseInt without radix to explicit radix

The `parseInt(str)` has been deprecated in favor of `parseInt(str, 10)`.

## Migration Guide

Always specify radix to avoid unexpected parsing

parseInt without radix can parse strings starting with 0 as octal.

## Before (Deprecated)

```javascript
parseInt("010")  // might be 8
```

## After (Modern)

```javascript
parseInt("010", 10)  // 10
parseInt("0x10", 16)  // 16
```

## Key Differences

- Always specify radix parameter
- 10 for decimal, 16 for hex
