---
title: "[Solution] Deprecated Function Migration: eval() to Function constructor"
description: "Migrate from deprecated eval() to safer alternatives."
deprecated_function: "eval(code)"
replacement_function: "new Function(code)()"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: eval() to Function constructor

The `eval(code)` has been deprecated in favor of `new Function(code)()`.

## Migration Guide

eval is dangerous with untrusted input.

## Before (Deprecated)

```javascript
const result = eval('1 + 2');
```

## After (Modern)

```javascript
const result = new Function('return 1 + 2')();
```

## Key Differences

- eval is dangerous with untrusted input
