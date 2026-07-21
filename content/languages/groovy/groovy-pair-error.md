---
title: "[Solution] Groovy Pair Error"
description: "Pair creation errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Pair Error

Pair creation errors.

### Common Causes
Wrong syntax; not in map

### How to Fix
```groovy
def pair = new Pair('key', 'value')
println pair.key
```

### Examples
```groovy
def map = [new Pair('a', 1), new Pair('b', 2)].collectEntries()
```
