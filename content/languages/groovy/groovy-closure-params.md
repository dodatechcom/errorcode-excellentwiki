---
title: "[Solution] Groovy Closure Parameter"
description: "Closure parameter type errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Closure Parameter

Closure parameter type errors.

### Common Causes
Wrong parameter count; implicit it

### How to Fix
```groovy
def greet = { String name -> println "Hello, $name" }
greet("World")
```

### Examples
```groovy
[1, 2, 3].each { println it }
[1, 2, 3].each { num -> println num * 2 }
```
