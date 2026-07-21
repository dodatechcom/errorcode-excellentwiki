---
title: "[Solution] Groovy Logging Error"
description: "Logging errors in Groovy."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Logging Error

Logging errors in Groovy.

### Common Causes
Missing @Log; wrong level

### How to Fix
```groovy
@log4j
class MyClass {
    void doWork() {
        log.info "Starting work"
    }
}
```

### Examples
```groovy
@groovy.util.logging.Slf4j
class MyClass {
    void doWork() {
        log.info 'Processing'
    }
}
```
