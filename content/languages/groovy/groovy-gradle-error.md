---
title: "[Solution] Groovy Gradle Error"
description: "Gradle build script errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Gradle Error

Gradle build script errors.

### Common Causes
Wrong task; missing plugin; dependency

### How to Fix
```groovy
plugins {
    id 'groovy'
}
dependencies {
    implementation 'org.apache.groovy:groovy:4.0.15'
}
```

### Examples
```groovy
task hello {
    doLast {
        println 'Hello from Gradle!'
    }
}
```
