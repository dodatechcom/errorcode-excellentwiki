---
title: "[Solution] Groovy Destructuring"
description: "Map/list destructuring errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Destructuring

Map/list destructuring errors.

### Common Causes
Wrong variable count; wrong syntax

### How to Fix
```groovy
def (name, age) = ["John", 30]
println "$name is $age"
```

### Examples
```groovy
def map = [name: "John", age: 30]
def (n, a) = map.values()
```
