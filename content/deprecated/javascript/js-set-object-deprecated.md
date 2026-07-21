---
title: "[Solution] Deprecated Function Migration: {} as set to Set"
description: "Migrate from deprecated {} used as set to Set."
deprecated_function: "{}"
replacement_function: "new Set()"
languages: ["javascript"]
deprecated_since: "ES2015+"
---

# [Solution] Deprecated Function Migration: {} as set to Set

The `{}` has been deprecated in favor of `new Set()`.

## Migration Guide

Set handles uniqueness automatically.

## Before (Deprecated)

```javascript
const set = {};
set[item] = true;
if (item in set) { }
```

## After (Modern)

```javascript
const set = new Set();
set.add(item);
if (set.has(item)) { }
```

## Key Differences

- Set handles uniqueness automatically
