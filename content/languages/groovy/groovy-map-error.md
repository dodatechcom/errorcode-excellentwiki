---
title: "[Solution] Groovy Map Error"
description: "Map creation and access errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Map Error

Map creation and access errors.

### Common Causes
Wrong syntax; key not found

### How to Fix
```groovy
def map = [name: "John", age: 30]
println map.name
println map["name"]
```

### Examples
```groovy
map.each { key, value -> println "$key: $value" }
```
