---
title: "[Solution] Groovy String Interpolation"
description: "String interpolation errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy String Interpolation

String interpolation errors.

### Common Causes
Wrong quote type; missing $

### How to Fix
```groovy
// GString (interpolation)
def name = "World"
println "Hello, $name!"
println "Hello, ${name.toUpperCase()}!"
```

### Examples
```groovy
// Single quotes = no interpolation
println 'Hello, $name!'  // literal
```
