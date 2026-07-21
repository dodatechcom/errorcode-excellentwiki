---
title: "[Solution] Groovy Process Execution"
description: "Process execution errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Process Execution

Process execution errors.

### Common Causes
Wrong command; not reading output

### How to Fix
```groovy
"ls -la".execute().text
```

### Examples
```groovy
def process = ['ls', '-la'].execute()
process.waitFor()
println process.text
```
