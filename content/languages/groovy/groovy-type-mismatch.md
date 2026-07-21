---
title: "[Solution] Groovy Type Mismatch Error"
description: "Assignment or parameter type mismatch."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Type Mismatch Error

Assignment or parameter type mismatch.

### Common Causes
Wrong type; Groovy duck typing issues

### How to Fix
```groovy
String name = "hello"
int count = name.length()
```

### Examples
```groovy
def x = 42  // Groovy auto-selects type
x = x.toInteger()
```
