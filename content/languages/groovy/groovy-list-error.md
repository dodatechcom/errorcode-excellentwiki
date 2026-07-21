---
title: "[Solution] Groovy List Error"
description: "List creation and manipulation errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy List Error

List creation and manipulation errors.

### Common Causes
Wrong syntax; method not found

### How to Fix
```groovy
def list = [1, 2, 3, 4, 5]
println list.collect { it * 2 }
```

### Examples
```groovy
def filtered = list.findAll { it > 2 }
def sum = list.sum()
```
