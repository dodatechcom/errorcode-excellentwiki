---
title: "[Solution] Deprecated Function Migration: Function.bind for partial to arrow functions"
description: "Migrate from deprecated bind for partial application to arrow functions."
deprecated_function: "fn.bind(null, arg)"
replacement_function: "(arg) => fn(arg, otherArg)"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: Function.bind for partial to arrow functions

The `fn.bind(null, arg)` has been deprecated in favor of `(arg) => fn(arg, otherArg)`.

## Migration Guide

Arrow functions are cleaner.

## Before (Deprecated)

```javascript
const bound = fn.bind(null, 'hello');
```

## After (Modern)

```javascript
const bound = (x) => fn('hello', x);
```

## Key Differences

- Arrow functions are cleaner
