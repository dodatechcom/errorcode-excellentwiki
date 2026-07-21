---
title: "[Solution] Groovy Object Builder"
description: "ObjectBuilder and builder errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Object Builder

ObjectBuilder and builder errors.

### Common Causes
Missing properties; wrong method

### How to Fix
```groovy
def builder = new groovy.json.JsonBuilder()
builder {
    name 'John'
    age 30
}
println builder.toString()
```

### Examples
```groovy
def xmlBuilder = new groovy.xml.MarkupBuilder()
xmlBuilder.records {
    employee(id: 1) {
        name 'John'
    }
}
```
