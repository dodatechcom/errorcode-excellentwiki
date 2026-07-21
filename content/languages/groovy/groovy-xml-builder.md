---
title: "[Solution] Groovy MarkupBuilder"
description: "MarkupBuilder errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy MarkupBuilder

MarkupBuilder errors.

### Common Causes
Wrong syntax; missing closure

### How to Fix
```groovy
import groovy.xml.MarkupBuilder
def builder = new MarkupBuilder()
builder.html {
    head { title('Test') }
    body { h1('Hello') }
}
```

### Examples
```groovy
def xml = new MarkupBuilder()
xml.records {
    employee(name: 'John', id: 1)
}
```
