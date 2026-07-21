---
title: "[Solution] Deprecated Function Migration: Object.assign to spread syntax"
description: "Migrate from deprecated Object.assign to spread syntax for object copying in JavaScript."
deprecated_function: "Object.assign({}, obj)"
replacement_function: "{ ...obj }"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: Object.assign to spread syntax

The `Object.assign({}, obj)` has been deprecated in favor of `{ ...obj }`.

## Migration Guide

Spread syntax is more concise for copying and merging objects.

## Before (Deprecated)

```javascript
var merged = Object.assign({}, defaults, overrides);
var copy = Object.assign({}, original);
```

## After (Modern)

```javascript
const merged = { ...defaults, ...overrides };
const copy = { ...original };

// Shallow copy
const shallow = { ...original, newProp: "value" };
```

## Key Differences

- Spread syntax is more concise
- Same shallow copy behavior
- Works for arrays too: [...arr]
