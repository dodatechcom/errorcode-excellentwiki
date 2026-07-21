---
title: "[Solution] Groovy Receiver Error"
description: "Closure receiver errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Receiver Error

Closure receiver errors.

### Common Causes
Wrong delegate; owner vs delegate

### How to Fix
```groovy
obj.with {
    // 'this' is still the outer class
    // 'delegate' is obj
}
```

### Examples
```groovy
closure.resolveStrategy = Closure.DELEGATE_FIRST
```
