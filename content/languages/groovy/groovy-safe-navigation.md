---
title: "[Solution] Groovy Safe Navigation"
description: "Safe navigation operator errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Safe Navigation

Safe navigation operator errors.

### Common Causes
Wrong usage; not null-safe

### How to Fix
```groovy
def name = null
println name?.toUpperCase()  // prints null
```

### Examples
```groovy
def result = obj?.property?.method() ?: "default"
```
