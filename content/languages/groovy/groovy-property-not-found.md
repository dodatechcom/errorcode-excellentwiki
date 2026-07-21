---
title: "[Solution] Groovy Property Not Found"
description: "Property access on object fails."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Property Not Found

Property access on object fails.

### Common Causes
Missing getter/setter; wrong name; null

### How to Fix
```groovy
class Person {
    String name
    int age
}
def p = new Person(name: "John", age: 30)
println p.name
```

### Examples
```groovy
def map = [name: "John", age: 30]
println map.name
```
