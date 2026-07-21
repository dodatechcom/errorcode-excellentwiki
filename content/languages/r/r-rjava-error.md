---
title: "[Solution] R rJava JVM Error"
description: "rJava JVM initialization errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rJava JVM Error

rJava JVM initialization errors.

### Common Causes
JAVA_HOME not set; wrong Java version

### How to Fix
```r
library(rJava)
.jinit()
```

### Examples
```r
Sys.setenv(JAVA_HOME = "/usr/lib/jvm/java-11-openjdk")
library(rJava)
```
