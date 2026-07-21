---
title: "[Solution] Scala Polymorphic Function Type Error"
description: "Fix Scala 3 polymorphic function type errors when defining functions with type parameters."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Polymorphic function type errors occur when using [T] =>> T syntax incorrectly or when the polymorphic function cannot be inferred.

## Common Causes

- Wrong syntax for polymorphic function type
- Polymorphic function not generalizing properly
- Missing type parameter in polymorphic function
- Polymorphic function with conflicting constraints

## How to Fix

### 1. Use correct polymorphic function syntax

```scala
val polyId: [T] => T => T = [T] => (x: T) => x
println(polyId(42))     // 42
println(polyId("hello")) // hello
```

### 2. Define polymorphic function properly

```scala
def polymorphicMap[T, U](list: List[T])(f: [A] => A => A): List[U] =
  ???

val transform: [T] => List[T] => List[T] = [T] => (list: List[T]) => list.reverse
```

## Examples

```scala
val duplicate: [T] => (T, T) => (T, T) = [T] => (a: T, b: T) => (a, b)

val result = duplicate(1, 2)
println(s"Pair: ${result._1}, ${result._2}")

val strings = duplicate("hello", "world")
println(s"Strings: ${strings._1}, ${strings._2}")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)
