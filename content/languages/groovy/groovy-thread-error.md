---
title: "[Solution] Groovy Threading Error"
description: "Multi-threading errors in Groovy."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Threading Error

Multi-threading errors in Groovy.

### Common Causes
Shared state; wrong synchronization

### How to Fix
```groovy
def list = Collections.synchronizedList([])
(1..10).each { i ->
    Thread.start {
        list << i
    }
}
```

### Examples
```groovy
use (GroovyAsyncCategory) {
    task { longRunning() } then { result -> println result }
}
```
