---
title: "[Solution] Groovy Exception Error"
description: "Exception handling in Groovy."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Exception Error

Exception handling in Groovy.

### Common Causes
Missing try-catch; wrong exception type

### How to Fix
```groovy
try {
    riskyOperation()
} catch (IOException e) {
    log.error "IO error: ${e.message}"
} finally {
    cleanup()
}
```

### Examples
```groovy
def result = ['success', 'error'].with {
    try { doWork() } catch (Exception e) { 'error' }
}
```
