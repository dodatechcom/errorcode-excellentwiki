---
title: "[Solution] Scala ImplicitScopeError - Brief Description"
description: "Fix Scala implicit scope resolution errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1043
---

An implicit scope error occurs when the compiler cannot find an implicit value in scope.

## Common Causes

- Implicit value not imported
- Conflicting implicit values
- Missing import for extension methods

## How to Fix

Import implicits explicitly:

```scala
import scala.math.Ordering.Implicits._
def sorted[T: Ordering](list: List[T]): List[T] = list.sorted
```

Define in companion objects:

```scala
case class Money(amount: Double)
object Money {
  implicit val ordering: Ordering[Money] = Ordering.by(_.amount)
}
```

## Examples

```scala
trait JsonEncoder[T] {
  def encode(value: T): String
}
object JsonEncoder {
  implicit val stringEncoder: JsonEncoder[String] = (s: String) => s"\"$s\""
  implicit val intEncoder: JsonEncoder[Int] = (i: Int) => i.toString
}
```

## Related Errors

- [Scala ImplicitNotFound](/languages/scala/scala-implicit-not-found)
- [Scala ImplicitAmbiguity](/languages/scala/scala-implicits-ambiguity)
