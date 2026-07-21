---
title: "[Solution] Scala Using Clauses Error"
description: "Fix Scala 3 using clause errors when declaring context parameters in method signatures."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Using clause errors occur when using parameters are not properly provided or when the using keyword is used incorrectly.

## Common Causes

- Missing using parameter at call site
- Wrong ordering of using and regular parameters
- Using clause with wrong type
- Multiple using clauses conflicting

## How to Fix

### 1. Provide using parameters correctly

```scala
trait Config {
  def host: String
  def port: Int
}

def connect(config: Config)(using logger: Logger): Unit = {
  logger.log(s"Connecting to ${config.host}:${config.port}")
}
```

### 2. Use proper using syntax

```scala
def process(data: List[Int])(using ord: Ordering[Int]): List[Int] = {
  data.sorted
}

given Ordering[Int] = Ordering.Int
val sorted = process(List(3, 1, 2))
```

## Examples

```scala
trait Encoder[T] {
  def encode(t: T): String
}

given intEncoder: Encoder[Int] = new Encoder[Int] {
  def encode(t: Int): String = t.toString
}

def jsonEncode[T](value: T)(using enc: Encoder[T]): String = {
  s"""{"value": "${enc.encode(value)}"}"""
}

println(jsonEncode(42))
```

## Related Errors

- [Given using error](/languages/scala/scala-given-using-error)
- [Implicit not found error](/languages/scala/scala-implicit-not-found)
- [Type error](/languages/scala/scala-type-mismatch)
