---
title: "[Solution] Groovy Tuple Error"
description: "Tuple creation and usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Tuple Error

Tuple creation and usage errors.

### Common Causes
Wrong syntax; fixed size

### How to Fix
```groovy
def tuple = new Tuple(1, 'hello', 3.14)
println tuple[1]  // 'hello'
```

### Examples
```groovy
def (a, b, c) = new Tuple(1, 'hello', 3.14)
```
