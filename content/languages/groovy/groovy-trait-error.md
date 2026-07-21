---
title: "[Solution] Groovy Trait Error"
description: "Trait definition and usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Trait Error

Trait definition and usage errors.

### Common Causes
Missing @Override; wrong composition

### How to Fix
```groovy
trait Greeter {
    String greet() { "Hello, $name" }
}
class Person implements Greeter {
    String name
}
```

### Examples
```groovy
def p = new Person(name: "John")
println p.greet()
```
