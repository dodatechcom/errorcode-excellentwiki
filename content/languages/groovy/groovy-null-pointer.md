---
title: "[Solution] Groovy Null Pointer Error"
description: "NullPointerError on method call."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Null Pointer Error

NullPointerError on method call.

### Common Causes
Object is null; not null-safe

### How to Fix
```groovy
def name = null
println name?.toUpperCase()  // safe navigation
```

### Examples
```groovy
def result = obj?.method() ?: "default"
```
