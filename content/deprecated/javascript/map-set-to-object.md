---
title: "[Solution] Deprecated Function Migration: plain objects as maps to Map/Set"
description: "Migrate from deprecated object-as-map pattern to Map and Set in JavaScript."
deprecated_function: "Object as map/lookup"
replacement_function: "Map/Set"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: plain objects as maps to Map/Set

The `Object as map/lookup` has been deprecated in favor of `Map/Set`.

## Migration Guide

Map and Set handle non-string keys and preserve insertion order, unlike plain objects.

## Before (Deprecated)

```javascript
var cache = {};
cache["key1"] = "value1";
console.log(Object.keys(cache).length);
```

## After (Modern)

```javascript
const cache = new Map();
cache.set("key1", "value1");
cache.set("key2", "value2");
console.log(cache.size);

// Any type of key
cache.set(42, "number key");

const unique = new Set([1, 2, 2, 3]);
console.log(unique.size);  // 3
```

## Key Differences

- Map keys can be any type
- Map.size for count
- Set stores unique values
- Both preserve insertion order
