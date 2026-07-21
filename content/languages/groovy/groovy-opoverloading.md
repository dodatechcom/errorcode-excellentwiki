---
title: "[Solution] Groovy Operator Overloading"
description: "Operator overloading errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Operator Overloading

Operator overloading errors.

### Common Causes
Wrong method name; wrong operator

### How to Fix
```groovy
class Vector {
    double x, y
    Vector plus(Vector other) {
        new Vector(x + other.x, y + other.y)
    }
}
```

### Examples
```groovy
def v1 = new Vector(1, 2)
def v2 = new Vector(3, 4)
def v3 = v1 + v2
```
