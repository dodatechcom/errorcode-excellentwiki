---
title: "[Solution] Scala Implicit Not Found"
description: "Fix Scala 'implicit not found' error. Learn about implicit resolution, type classes, and providing implicit values in Scala."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `implicit not found` error occurs when the Scala compiler cannot find a required implicit value for a type class, context bound, or implicit parameter. This is a compile-time error that indicates missing evidence for a type.

## Common Causes

- Missing implicit instance for a type class
- Implicit not in scope
- Wrong implicit imported
- Type class not implemented for custom type
- Implicit ambiguity

## How to Fix

Define implicit instances:

```scala
trait Show[T] {
  def show(value: T): String
}

object Show {
  implicit val intShow: Show[Int] = new Show[Int] {
    def show(value: Int): String = value.toString
  }

  implicit val stringShow: Show[String] = new Show[String] {
    def show(value: String): String = s""""$value""""
  }
}

def printItem[T](item: T)(implicit s: Show[T]): Unit = {
  println(s.show(item))
}
```

Import implicits explicitly:

```scala
import MyImplicits._

printItem(42) // Uses intShow
```

Implement type class for custom types:

```scala
case class User(name: String, age: Int)

object User {
  implicit val userShow: Show[User] = new Show[User] {
    def show(user: User): String = s"${user.name} (${user.age})"
  }
}
```

Use context bounds:

```scala
def process[T: Show](item: T): Unit = {
  println(implicitly[Show[T]].show(item))
}
```

## Examples

```scala
def foo[T](x: T)(implicit ev: Numeric[T]) = ev.plus(x, x)
foo("hello") // error: could not find implicit value for evidence parameter ev: Numeric[String]
```

## Related Errors

- [typeerror] — type mismatch errors
- [matcherror] — pattern match fails
