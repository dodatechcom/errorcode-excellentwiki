---
title: "[Solution] Groovy Mock Error"
description: "Spock mocking errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Mock Error

Spock mocking errors.

### Common Causes
Wrong mock type; missing interaction

### How to Fix
```groovy
def service = Mock(MyService)
def result = service.getData()
1 * service.getData() >> 'mocked data'
```

### Examples
```groovy
def collaborator = Mock(Collaborator)
def obj = new MyClass(collaborator)
collaborator.doWork() >> 'done'
obj.execute()
1 * collaborator.doWork()
```
