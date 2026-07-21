---
title: "[Solution] Scala Given/Using Error"
description: "Fix Scala 3 given/using errors when using context parameters for dependency injection."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Given/using errors occur when implicit values are not properly provided or when given instances have ambiguous resolution.

## Common Causes

- Missing given instance for required context parameter
- Ambiguous given instances in scope
- Wrong given syntax
- Using given from wrong scope

## How to Fix

### 1. Define given instances correctly

```scala
given ordering: Ordering[Int] = Ordering.Int
def sorted[T](list: List[T])(using ord: Ordering[T]): List[T] = list.sorted
```

### 2. Provide using parameters

```scala
trait Logger {
  def log(msg: String): Unit
}

given ConsoleLogger: Logger with {
  def log(msg: String): Unit = println(msg)
}

def process(msg: String)(using logger: Logger): Unit = {
  logger.log(msg)
}
```

## Examples

```scala
trait Encoder[T] {
  def encode(value: T): String
}

given intEncoder: Encoder[Int] with {
  def encode(value: Int): String = value.toString
}

given stringEncoder: Encoder[String] with {
  def encode(value: String): String = s"\"$value\""
}

def display[T](value: T)(using enc: Encoder[T]): Unit = {
  println(s"Encoded: ${enc.encode(value)}")
}

display(42)
display("hello")
```

## Related Errors

- [Implicit not found error](/languages/scala/scala-implicit-not-found)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
