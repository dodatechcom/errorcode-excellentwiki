---
title: "MetaClass error in Groovy"
description: "Fix MetaClass errors when dynamically adding or modifying methods/properties on classes at runtime."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["metaclass", "dynamic", "runtime", "groovy", "method-missing"]
weight: 5
---

## What This Error Means

Groovy's MetaClass system allows runtime modification of class behavior. Errors occur when attempting to add methods or properties that conflict with existing definitions.

## Common Causes

- Adding a method that already exists without proper override
- MetaClass modification on final classes
- Method signature conflicts
- Thread-safety issues with MetaClass changes

## How to Fix

```groovy
// WRONG: Conflicting MetaClass method
String.metaClass.foo = { -> "bar" }
String.metaClass.foo = { -> "baz" }

// CORRECT: Use a unique method name
String.metaClass.getFoo = { -> "bar" }
```

```groovy
// WRONG: Modifying final class MetaClass
Integer.metaClass.timesTwo = { delegate * 2 }

// CORRECT: Use extension methods
def timesTwo = { Integer n -> n * 2 }
println timesTwo(5)   // 10
```

## Examples

```groovy
String.metaClass.shout = { delegate.toUpperCase() + "!!" }
println "hello".shout()   // HELLO!!
```

## Related Errors

- [MissingMethodException](/languages/groovy/missing-method) - method resolution
- [MissingPropertyException](/languages/groovy/missing-property) - property resolution
