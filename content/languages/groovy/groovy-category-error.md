---
title: "[Solution] Groovy Category Error"
description: "Category usage errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Category Error

Category usage errors.

### Common Causes
Missing use statement; wrong methods

### How to Fix
```groovy
use (StringCategory) {
    println "hello".shout()
}
```

### Examples
```groovy
@Category(String)
class StringCategory {
    String shout() { this.toUpperCase() + "!" }
}
```
