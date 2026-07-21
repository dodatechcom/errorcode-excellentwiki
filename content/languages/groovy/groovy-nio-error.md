---
title: "[Solution] Groovy NIO Error"
description: "NIO file operations errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy NIO Error

NIO file operations errors.

### Common Causes
Wrong path; encoding; permissions

### How to Fix
```groovy
import java.nio.file.*
def path = Paths.get('data.txt')
def lines = Files.readAllLines(path)
```

### Examples
```groovy
Files.write(Paths.get('output.txt'), ['line1', 'line2'])
```
