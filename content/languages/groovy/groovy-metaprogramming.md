---
title: "[Solution] Groovy Metaprogramming"
description: "MetaClass and metaprogramming errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Metaprogramming

MetaClass and metaprogramming errors.

### Common Causes
Wrong invocation; method not found at runtime

### How to Fix
```groovy
String.metaClass.shout = { -> delegate.toUpperCase() + "!" }
println "hello".shout()
```

### Examples
```groovy
obj.metaClass.myMethod = { -> "result" }
println obj.myMethod()
```
