---
title: "[Solution] Groovy CompletableFuture"
description: "CompletableFuture errors in Groovy."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy CompletableFuture

CompletableFuture errors in Groovy.

### Common Causes
Missing thenApply; wrong chaining

### How to Fix
```groovy
import java.util.concurrent.CompletableFuture
CompletableFuture.supplyAsync {
    'result'
}.thenApply { it.toUpperCase() }
```

### Examples
```groovy
CompletableFuture.supplyAsync {
    computeValue()
}.thenAccept { println it }
```
