---
title: "[Solution] Deprecated Function Migration: Object.create(null) for dict to Map"
description: "Migrate from deprecated Object.create(null) dictionary pattern to Map."
deprecated_function: "Object.create(null)"
replacement_function: "new Map()"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: Object.create(null) for dict to Map

The `Object.create(null)` has been deprecated in favor of `new Map()`.

## Migration Guide

Map provides better performance for frequent additions/deletions

Object.create(null) creates objects without prototype. Map is better for dynamic key-value storage.

## Before (Deprecated)

```javascript
const dict = Object.create(null);
dict["key"] = "value";
if ("key" in dict) { /* ... */ }
```

## After (Modern)

```javascript
const map = new Map();
map.set("key", "value");
if (map.has("key")) { /* ... */ }
console.log(map.size);
```

## Key Differences

- Map has size property
- Map supports any type as key
- Map has built-in has/get/set/delete
- Better performance for frequent modifications
