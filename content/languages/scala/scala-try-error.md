---
title: "[Solution] Scala TryError - Brief Description"
description: "Fix Scala Try errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1053
---

A Try error occurs when exception handling does not cover all cases.

## Common Causes

- Calling `.get` on a failed `Try`
- Not handling the `Failure` case

## How to Fix

Pattern match:

```scala
import scala.util.{Try, Success, Failure}
val result: Try[Int] = Try("42".toInt)
result match {
  case Success(value) => println(s"Got: $value")
  case Failure(ex) => println(s"Failed: ${ex.getMessage}")
}
```

Use recover:

```scala
val safeResult = Try("42".toInt)
  .recover { case _: NumberFormatException => 0 }
  .getOrElse(0)
```

## Examples

```scala
import scala.util.{Try, Success, Failure}
def divide(a: Int, b: Int): Try[Double] = Try(a.toDouble / b)
divide(10, 2) // Success(5.0)
divide(10, 0) // Failure(ArithmeticException)
```

## Related Errors

- [Scala EitherError](/languages/scala/scala-either-error)
- [Scala OptionGetError](/languages/scala/scala-option-get-error)
