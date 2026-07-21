---
title: "[Solution] Deprecated Function Migration: {} as map to Map"
description: "Migrate from deprecated {} used as map to Map."
deprecated_function: "{}"
replacement_function: "new Map()"
languages: ["javascript"]
deprecated_since: "ES2015+"
---

# [Solution] Deprecated Function Migration: {} as map to Map

The `{}` has been deprecated in favor of `new Map()`.

## Migration Guide

Map has better performance for frequent additions/deletions.

## Before (Deprecated)

```javascript
const map = {};
map[key] = value;
delete map[key];
```

## After (Modern)

```javascript
const map = new Map();
map.set(key, value);
map.delete(key);
```

## Key Differences

- Map is better for frequent changes
