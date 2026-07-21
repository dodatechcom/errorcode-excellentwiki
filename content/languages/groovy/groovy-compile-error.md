---
title: "[Solution] Groovy Compile Error"
description: "Compile-time errors in Groovy scripts."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Compile Error

Compile-time errors in Groovy scripts.

### Common Causes
Wrong type; missing semicolons; syntax

### How to Fix
```groovy
@groovy.transform.CompileStatic
def add(int a, int b) { a + b }
```

### Examples
```groovy
@groovy.transform.TypeChecked
def divide(int a, int b) { a / b }
```
