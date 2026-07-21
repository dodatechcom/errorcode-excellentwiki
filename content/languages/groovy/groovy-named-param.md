---
title: "[Solution] Groovy Named Parameters"
description: "Named parameter errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Named Parameters

Named parameter errors.

### Common Causes
Wrong parameter order; missing @Named

### How to Fix
```groovy
def greet(String name, int age = 0) {
    println "$name is $age"
}
greet(name: "John", age: 30)
```

### Examples
```groovy
@NamedVariant
void process(String input, int count = 1) { ... }
```
