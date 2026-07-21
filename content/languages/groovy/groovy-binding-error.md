---
title: "[Solution] Groovy Binding Error"
description: "Script binding and variable scope errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Binding Error

Script binding and variable scope errors.

### Common Causes
Wrong scope; missing binding

### How to Fix
```groovy
binding.setVariable('myVar', 'value')
def result = binding.getVariable('myVar')
```

### Examples
```groovy
// In script
this.binding.myVar = 'value'
```
