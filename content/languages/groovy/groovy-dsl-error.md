---
title: "[Solution] Groovy DSL Error"
description: "DSL (Domain Specific Language) errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy DSL Error

DSL (Domain Specific Language) errors.

### Common Causes
Missing delegate; wrong closure delegation

### How to Fix
```groovy
class MyBuilder {
    def result = [:]
    def methodMissing(String name, args) {
        result[name] = args[0]
    }
}
```

### Examples
```groovy
def builder = new MyBuilder()
builder.with {
    name "Test"
    value 42
}
```
