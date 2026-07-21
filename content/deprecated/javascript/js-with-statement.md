---
title: "[Solution] Deprecated Function Migration: with statement to explicit property access"
description: "Migrate from deprecated with statement to explicit property access."
deprecated_function: "with (obj) { ... }"
replacement_function: "obj.prop"
languages: ["javascript"]
deprecated_since: "Strict Mode"
---

# [Solution] Deprecated Function Migration: with statement to explicit property access

The `with (obj) { ... }` has been deprecated in favor of `obj.prop`.

## Migration Guide

with is forbidden in strict mode and causes performance issues

The with statement is deprecated and forbidden in strict mode. Use explicit property access.

## Before (Deprecated)

```javascript
with (document.forms[0]) {
    elements["name"].value = "Alice";
    elements["age"].value = 30;
}
```

## After (Modern)

```javascript
const form = document.forms[0];
form.elements["name"].value = "Alice";
form.elements["age"].value = 30;

// Or with destructuring
const { name, age } = form.elements;
```

## Key Differences

- with is forbidden in strict mode
- Explicit access is clearer
- Better performance (no scope chain)
- IDE support for autocompletion
