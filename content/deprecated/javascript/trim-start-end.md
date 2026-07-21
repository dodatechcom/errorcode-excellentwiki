---
title: "[Solution] Deprecated Function Migration: trimLeft/trimRight to trimStart/trimEnd"
description: "Migrate from deprecated String.trimLeft/trimRight to String.trimStart/trimEnd in JavaScript."
deprecated_function: "str.trimLeft()"
replacement_function: "str.trimStart()"
languages: ["javascript"]
deprecated_since: "ES2019"
---

# [Solution] Deprecated Function Migration: trimLeft/trimRight to trimStart/trimEnd

The `str.trimLeft()` has been deprecated in favor of `str.trimStart()`.

## Migration Guide

trimStart and trimEnd are the standardized names in ES2019.

## Before (Deprecated)

```javascript
const str = "  Hello, World!  ";
console.log(str.trimLeft());
console.log(str.trimRight());
```

## After (Modern)

```javascript
const str = "  Hello, World!  ";
console.log(str.trimStart());
console.log(str.trimEnd());
console.log(str.trim());
```

## Key Differences

- trimLeft -> trimStart
- trimRight -> trimEnd
- trim() trims both ends
