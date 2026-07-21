---
title: "[Solution] Groovy Default Parameters"
description: "Default parameter errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Default Parameters

Default parameter errors.

### Common Causes
Wrong position; not optional

### How to Fix
```groovy
def greet(String name, String greeting = "Hello") {
    "$greeting, $name!"
}
```

### Examples
```groovy
def divide(double a, double b = 1.0) {
    a / b
}
```
