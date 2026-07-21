---
title: "[Solution] Deprecated Function Migration: instanceof Array to Array.isArray"
description: "Migrate from deprecated instanceof Array to Array.isArray."
deprecated_function: "arr instanceof Array"
replacement_function: "Array.isArray(arr)"
languages: ["javascript"]
deprecated_since: "ES5.1+"
---

# [Solution] Deprecated Function Migration: instanceof Array to Array.isArray

The `arr instanceof Array` has been deprecated in favor of `Array.isArray(arr)`.

## Migration Guide

Array.isArray works across iframes

instanceof Array fails across iframe boundaries.

## Before (Deprecated)

```javascript
if (arr instanceof Array) { }
```

## After (Modern)

```javascript
if (Array.isArray(arr)) { }
```

## Key Differences

- Array.isArray works across iframes
- instanceof can fail with multiple realms
