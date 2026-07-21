---
title: "[Solution] Deprecated Function Migration: obj.toString() override to Symbol.toStringTag"
description: "Migrate from deprecated toString override to Symbol.toStringTag."
deprecated_function: "obj.toString = function() { }"
replacement_function: "[Symbol.toStringTag]: 'MyClass'"
languages: ["javascript"]
deprecated_since: "ES2015+"
---

# [Solution] Deprecated Function Migration: obj.toString() override to Symbol.toStringTag

The `obj.toString = function() { }` has been deprecated in favor of `[Symbol.toStringTag]: 'MyClass'`.

## Migration Guide

Symbol.toStringTag is cleaner.

## Before (Deprecated)

```javascript
function MyClass() { }
MyClass.prototype.toString = function() { return 'MyClass'; };
```

## After (Modern)

```javascript
class MyClass {
    get [Symbol.toStringTag]() {
        return 'MyClass';
    }
}
```

## Key Differences

- Symbol.toStringTag is cleaner
