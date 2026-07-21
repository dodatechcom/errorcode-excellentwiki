---
title: "[Solution] Groovy Variable Swap"
description: "Variable swap syntax errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Variable Swap

Variable swap syntax errors.

### Common Causes
Wrong syntax; not using tuple

### How to Fix
```groovy
(a, b) = (b, a)  // Groovy swap
```

### Examples
```groovy
def (a, b) = [1, 2]
println "a=$a, b=$b"
```
