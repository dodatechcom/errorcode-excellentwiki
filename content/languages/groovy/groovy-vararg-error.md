---
title: "[Solution] Groovy Varargs Error"
description: "Varargs parameter errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Varargs Error

Varargs parameter errors.

### Common Causes
Wrong syntax; array vs varargs

### How to Fix
```groovy
def sum(int... numbers) {
    numbers.sum()
}
println sum(1, 2, 3, 4)
```

### Examples
```groovy
def join(String... parts) {
    parts.join(', ')
}
println join('a', 'b', 'c')
```
