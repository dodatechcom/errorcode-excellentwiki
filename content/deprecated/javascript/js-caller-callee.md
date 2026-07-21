---
title: "[Solution] Deprecated Function Migration: arguments.callee to named functions"
description: "Migrate from deprecated arguments.callee to named functions."
deprecated_function: "arguments.callee"
replacement_function: "function name() {}"
languages: ["javascript"]
deprecated_since: "Strict Mode"
---

# [Solution] Deprecated Function Migration: arguments.callee to named functions

The `arguments.callee` has been deprecated in favor of `function name() {}`.

## Migration Guide

arguments.callee is forbidden in strict mode

arguments.callee is deprecated and forbidden in strict mode.

## Before (Deprecated)

```javascript
function factorial(n) {
    if (n <= 1) return 1;
    return n * arguments.callee(n - 1);
}
```

## After (Modern)

```javascript
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

## Key Differences

- Named functions are clearer
- arguments.callee is forbidden in strict mode
