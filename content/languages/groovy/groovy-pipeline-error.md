---
title: "[Solution] Groovy Pipeline Error"
description: "Pipeline and chaining errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Pipeline Error

Pipeline and chaining errors.

### Common Causes
Wrong operator; not chaining

### How to Fix
```groovy
[1, 2, 3].findAll { it > 1 }.collect { it * 2 }.sum()
```

### Examples
```groovy
def result = people
    .findAll { it.age > 18 }
    .collect { it.name }
    .sort()
```
