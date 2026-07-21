---
title: "[Solution] Groovy Elvis Operator"
description: "Elvis operator usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Elvis Operator

Elvis operator usage errors.

### Common Causes
Wrong syntax; not providing default

### How to Fix
```groovy
def name = null
def displayName = name ?: "Anonymous"
```

### Examples
```groovy
def value = map.key ?: "default"
```
