---
title: "[Solution] Deprecated Function Migration: __proto__ to Object.getPrototypeOf"
description: "Migrate from deprecated __proto__ to standard prototype methods."
deprecated_function: "obj.__proto__"
replacement_function: "Object.getPrototypeOf(obj)"
languages: ["javascript"]
deprecated_since: "ES5.1+"
---

# [Solution] Deprecated Function Migration: __proto__ to Object.getPrototypeOf

The `obj.__proto__` has been deprecated in favor of `Object.getPrototypeOf(obj)`.

## Migration Guide

__proto__ is non-standard; use standard methods

__proto__ is non-standard.

## Before (Deprecated)

```javascript
const proto = obj.__proto__;
```

## After (Modern)

```javascript
const proto = Object.getPrototypeOf(obj);
Object.setPrototypeOf(obj, newProto);
const obj = Object.create(proto);
```

## Key Differences

- __proto__ is non-standard
- Object.getPrototypeOf is the standard
- Object.create for creating with prototype
