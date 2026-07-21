---
title: "[Solution] Groovy FileSystem Error"
description: "File operations errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy FileSystem Error

File operations errors.

### Common Causes
Wrong path; permissions; encoding

### How to Fix
```groovy
def file = new File('test.txt')
file.text = 'Hello World'
def content = file.text
```

### Examples
```groovy
file.eachLine { line -> println line }
file.append('appended text')
```
