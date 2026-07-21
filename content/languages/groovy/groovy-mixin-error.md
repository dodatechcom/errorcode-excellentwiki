---
title: "[Solution] Groovy Mixin Error"
description: "Mixin usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Mixin Error

Mixin usage errors.

### Common Causes
Deprecated; use traits instead

### How to Fix
```groovy
// Mixin is deprecated - use traits
trait MyTrait {
    def myMethod() { 'result' }
}
```

### Examples
```groovy
class MyClass implements MyTrait {
    // inherits myMethod
}
```
