---
title: "[Solution] Scala TypeInferenceError - Brief Description"
description: "Fix Scala type inference errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1044
---

A type inference error occurs when the compiler cannot determine the type automatically.

## Common Causes

- Complex nested generic types
- Recursive type definitions without bounds
- Missing return type on recursive functions

## How to Fix

Add explicit type annotations:

```scala
def process[T](items: List[T]): Map[T, Int] = {
  items.groupBy(identity).map { case (k, v) => (k, v.length) }
}
```

Annotate recursive functions:

```scala
def factorial(n: Int): Int = n match {
  case 0 => 1
  case _ => n * factorial(n - 1)
}
```

## Examples

```scala
val map: Map[String, List[Int]] = Map(
  "a" -> List(1, 2),
  "b" -> List(3, 4)
)
```

## Related Errors

- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
- [Scala ImplicitNotFound](/languages/scala/scala-implicit-not-found)
