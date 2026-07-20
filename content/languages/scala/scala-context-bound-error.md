---
title: "[Solution] Scala ContextBoundError - Brief Description"
description: "Fix Scala context bound errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1049
---

A context bound error occurs when no implicit instance of the type class is available.

## Common Causes

- Missing implicit instance for required type class
- Type class not imported into scope

## How to Fix

Provide implicit instances:

```scala
trait JsonEncoder[T] { def encode(value: T): String }
object JsonEncoder {
  implicit val intEncoder: JsonEncoder[Int] = (i: Int) => i.toString
  implicit val stringEncoder: JsonEncoder[String] = (s: String) => s"\"$s\""
}
def toJson[T: JsonEncoder](value: T): String = {
  implicitly[JsonEncoder[T]].encode(value)
}
```

## Examples

```scala
trait Show[T] { def show(value: T): String }
object Show {
  implicit val intShow: Show[Int] = (i: Int) => s"Int($i)"
}
def display[T: Show](value: T): Unit = println(implicitly[Show[T]].show(value))
```

## Related Errors

- [Scala ImplicitNotFound](/languages/scala/scala-implicit-not-found)
- [Scala ImplicitAmbiguity](/languages/scala/scala-implicits-ambiguity)
