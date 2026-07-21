---
title: "[Solution] Scala Given Instance Error"
description: "Fix Scala 3 given instance definition errors when providing implicit values."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Given instance errors occur when given instances are defined incorrectly or when they conflict with other given instances.

## Common Causes

- Wrong given syntax
- Multiple given instances of same type
- Given instance with wrong type
- Given not accessible from using site

## How to Fix

### 1. Define given instances correctly

```scala
trait Show[T] {
  def show(t: T): String
}

given Show[Int] with {
  def show(t: Int): String = t.toString
}

given Show[String] with {
  def show(t: String): String = s"\"$t\""
}
```

### 2. Use given with using

```scala
def printItem[T](item: T)(using s: Show[T]): Unit = {
  println(s.show(item))
}

printItem(42)
printItem("hello")
```

## Examples

```scala
trait Validator[T] {
  def validate(t: T): Boolean
}

given Validator[Int] with {
  def validate(t: Int): Boolean = t >= 0
}

given Validator[String] with {
  def validate(t: String): Boolean = t.nonEmpty
}

def check[T](value: T)(using v: Validator[T]): Boolean = v.validate(value)

println(check(42))     // true
println(check(-1))     // false
println(check("hello")) // true
```

## Related Errors

- [Given using error](/languages/scala/scala-given-using-error)
- [Implicit not found error](/languages/scala/scala-implicit-not-found)
- [Type error](/languages/scala/scala-type-mismatch)
