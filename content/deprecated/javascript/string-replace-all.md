---
title: "[Solution] Deprecated Function Migration: replace with regex g flag to replaceAll"
description: "Migrate from deprecated replace with /g flag to String.replaceAll in JavaScript."
deprecated_function: "str.replace(/pattern/g, replacement)"
replacement_function: "str.replaceAll(pattern, replacement)"
languages: ["javascript"]
deprecated_since: "ES2021"
---

# [Solution] Deprecated Function Migration: replace with regex g flag to replaceAll

The `str.replace(/pattern/g, replacement)` has been deprecated in favor of `str.replaceAll(pattern, replacement)`.

## Migration Guide

replaceAll is more explicit and does not require regex for simple string replacements.

## Before (Deprecated)

```javascript
const str = "Hello World World";
const result = str.replace(/World/g, "Earth");
```

## After (Modern)

```javascript
const str = "Hello World World";
const result = str.replaceAll("World", "Earth");

// With regex
const result2 = str.replaceAll(/World/g, "Earth");
```

## Key Differences

- replaceAll takes a string directly
- No need for regex g flag
- More readable for simple replacements
