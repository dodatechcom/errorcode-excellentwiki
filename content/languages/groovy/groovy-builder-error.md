---
title: "[Solution] Groovy Builder Pattern"
description: "Builder pattern errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Builder Pattern

Builder pattern errors.

### Common Causes
Wrong method; missing build

### How to Fix
```groovy
class PersonBuilder {
    String name
    int age
    Person build() { new Person(name, age) }
}
```

### Examples
```groovy
def person = new PersonBuilder()
    .name("John")
    .age(30)
    .build()
```
