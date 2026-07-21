---
title: "[Solution] Groovy Expando Error"
description: "Expando dynamic object errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Expando Error

Expando dynamic object errors.

### Common Causes
Wrong property; method not defined

### How to Fix
```groovy
def exp = new Expando()
exp.name = "Test"
exp.greet = { -> "Hello, $name" }
println exp.greet()
```

### Examples
```groovy
def exp = new Expando()
exp.calculate = { a, b -> a + b }
println exp.calculate(3, 4)
```
