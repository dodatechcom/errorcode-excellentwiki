---
title: "[Solution] Deprecated Function Migration: for...in with hasOwnProperty to Object.keys"
description: "Migrate from deprecated for...in with hasOwnProperty check to Object.keys."
deprecated_function: "for...in with hasOwnProperty"
replacement_function: "Object.keys/Object.entries"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: for...in with hasOwnProperty to Object.keys

The `for...in with hasOwnProperty` has been deprecated in favor of `Object.keys/Object.entries`.

## Migration Guide

Object.keys avoids prototype properties

for...in iterates prototype properties.

## Before (Deprecated)

```javascript
for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
        console.log(key, obj[key]);
    }
}
```

## After (Modern)

```javascript
for (const key of Object.keys(obj)) {
    console.log(key, obj[key]);
}

for (const [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
```

## Key Differences

- Object.keys for own enumerable keys
- Object.values for values
- Object.entries for key-value pairs
