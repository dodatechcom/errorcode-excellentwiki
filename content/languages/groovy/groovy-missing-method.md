---
title: "[Solution] Groovy Missing Method"
description: "Method not found on object."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Missing Method

Method not found on object.

### Common Causes
Wrong method name; missing property; typo

### How to Fix
```groovy
obj.metaClass.myMethod = { -> "result" }
```

### Examples
```groovy
"hello".capitalize()
[1,2,3].collect { it * 2 }
```
