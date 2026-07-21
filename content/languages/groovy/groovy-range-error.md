---
title: "[Solution] Groovy Range Error"
description: "Range creation and usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Range Error

Range creation and usage errors.

### Common Causes
Wrong syntax; exclusive vs inclusive

### How to Fix
```groovy
def range = 1..10  // inclusive
def exclusive = 1..<10  // exclusive
```

### Examples
```groovy
range.each { println it }
def subRange = range[2..5]
```
