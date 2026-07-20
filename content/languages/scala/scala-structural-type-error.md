---
title: "[Solution] Scala StructuralTypeError - Brief Description"
description: "Fix Scala structural type errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1046
---

A structural type error occurs when using duck typing and reflection fails.

## Common Causes

- Method not available at runtime
- Missing `-Xreflective-callables` compiler flag
- Security restrictions blocking reflection

## How to Fix

Enable reflective callables:

```scala
scalacOptions += "-Xreflective-callables"
```

Define structural type explicitly:

```scala
def greet(obj: { def name: String; def age: Int }): String = {
  s"Hello ${obj.name}, age ${obj.age}"
}
```

## Examples

```scala
trait Speakable { def speak(): String }
def makeNoise(obj: { def speak(): String }): String = obj.speak()
```

## Related Errors

- [Scala CompoundTypeError](/languages/scala/scala-compound-type-error)
- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
