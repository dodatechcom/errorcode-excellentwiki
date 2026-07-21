---
title: "[Solution] Groovy Truthiness Error"
description: "Groovy truth evaluation errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Truthiness Error

Groovy truth evaluation errors.

### Common Causes
Empty collections; zero is falsy

### How to Fix
```groovy
if (list) { println "Not empty" }  // truthy if non-empty
if (str) { println "Non-empty" }  // truthy if non-empty
```

### Examples
```groovy
def x = 0
if (x) { println "truthy" } else { println "falsy" }  // falsy
```
