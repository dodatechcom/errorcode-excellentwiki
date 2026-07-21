---
title: "[Solution] Groovy Ant Error"
description: "AntBuilder errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Ant Error

AntBuilder errors.

### Common Causes
Wrong task; missing import

### How to Fix
```groovy
import groovy.ant.AntBuilder
ant = new AntBuilder()
ant.copy(file: 'src.txt', tofile: 'dst.txt')
```

### Examples
```groovy
ant.mkdir(dir: 'build/classes')
ant.javac(srcdir: 'src', destdir: 'build/classes')
```
