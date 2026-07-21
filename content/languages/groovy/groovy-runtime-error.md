---
title: "[Solution] Groovy Runtime Error"
description: "Runtime type errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Runtime Error

Runtime type errors.

### Common Causes
Missing property; wrong method call

### How to Fix
```groovy
def obj = [name: "test"]
println obj?.name
```

### Examples
```groovy
def list = [1, 2, 3]
list.collect { it * 2 }.findAll { it > 2 }
```
