---
title: "[Solution] Groovy Spread Operator"
description: "Spread operator usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Spread Operator

Spread operator usage errors.

### Common Causes
Wrong syntax; null elements

### How to Fix
```groovy
def names = ["Alice", "Bob"]
def upper = names*.toUpperCase()
```

### Examples
```groovy
def people = [[name:"Alice"], [name:"Bob"]]
def names = people*.name
```
