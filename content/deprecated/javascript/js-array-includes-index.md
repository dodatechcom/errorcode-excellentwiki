---
title: "[Solution] Deprecated Function Migration: indexOf !== -1 to includes"
description: "Migrate from deprecated indexOf pattern to includes."
deprecated_function: "arr.indexOf(item) !== -1"
replacement_function: "arr.includes(item)"
languages: ["javascript"]
deprecated_since: "ES2016"
---

# [Solution] Deprecated Function Migration: indexOf !== -1 to includes

The `arr.indexOf(item) !== -1` has been deprecated in favor of `arr.includes(item)`.

## Migration Guide

includes returns boolean directly.

## Before (Deprecated)

```javascript
if (arr.indexOf(item) !== -1) { }
```

## After (Modern)

```javascript
if (arr.includes(item)) { }
```

## Key Differences

- includes returns boolean
