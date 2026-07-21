---
title: "[Solution] Gradle Task Error"
description: "Gradle task definition errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Gradle Task Error

Gradle task definition errors.

### Common Causes
Missing doLast; wrong configuration

### How to Fix
```groovy
task compile {
    doLast {
        println 'Compiling...'
    }
}
```

### Examples
```groovy
tasks.register('hello') {
    doLast {
        println 'Hello!'
    }
}
```
