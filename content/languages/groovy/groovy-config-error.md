---
title: "[Solution] Groovy ConfigSlurper"
description: "ConfigSlurper parsing errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy ConfigSlurper

ConfigSlurper parsing errors.

### Common Causes
Wrong format; environment issues

### How to Fix
```groovy
import groovy.util.ConfigSlurper
def config = new ConfigSlurper().parse('app.name="Test"')
println config.app.name
```

### Examples
```groovy
config.with {
    app {
        name = 'MyApp'
        version = '1.0'
    }
}
```
