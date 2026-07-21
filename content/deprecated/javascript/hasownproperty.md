---
title: "[Solution] Deprecated Function Migration: hasOwnProperty in for...in to Object.hasOwn"
description: "Migrate from deprecated hasOwnProperty pattern to Object.hasOwn() in JavaScript."
deprecated_function: "obj.hasOwnProperty(key)"
replacement_function: "Object.hasOwn(obj, key)"
languages: ["javascript"]
deprecated_since: "ES2022"
---

# [Solution] Deprecated Function Migration: hasOwnProperty in for...in to Object.hasOwn

The `obj.hasOwnProperty(key)` has been deprecated in favor of `Object.hasOwn(obj, key)`.

## Migration Guide

Object.hasOwn() is the modern replacement that works directly on the object without prototype concerns.

## Before (Deprecated)

```javascript
for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
        console.log(key, obj[key]);
    }
}
```

## After (Modern)

```javascript
// Object.hasOwn -- no prototype concern
if (Object.hasOwn(obj, key)) {
    console.log(key, obj[key]);
}

// Or use Object.keys for iteration
for (const key of Object.keys(obj)) {
    console.log(key, obj[key]);
}
```

## Key Differences

- Object.hasOwn() is more reliable
- Does not rely on prototype chain
- Works with objects without prototype
- Prefer Object.keys/values/entries for iteration
