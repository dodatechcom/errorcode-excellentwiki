---
title: "[Solution] Groovy Syntax Error"
description: "Groovy parser encounters invalid syntax."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Syntax Error

Groovy parser encounters invalid syntax.

### Common Causes
Missing brace; wrong operator; typo

### How to Fix
```groovy
def name = "World"
println "Hello, $name!"
```

### Examples
```groovy
def list = [1, 2, 3]
list.each { println it }
```
