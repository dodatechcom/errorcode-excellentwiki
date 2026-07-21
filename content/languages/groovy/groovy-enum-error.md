---
title: "[Solution] Groovy Enum Error"
description: "Enum definition and usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Enum Error

Enum definition and usage errors.

### Common Causes
Wrong values; missing methods

### How to Fix
```groovy
enum Color {
    RED, GREEN, BLUE
}
```

### Examples
```groovy
enum Planet {
    MERCURY(3.303e+23, 2.4397e6),
    VENUS(4.869e+24, 6.0518e6)
    final double mass
    final double radius
    Planet(double mass, double radius) {
        this.mass = mass
        this.radius = radius
    }
}
```
