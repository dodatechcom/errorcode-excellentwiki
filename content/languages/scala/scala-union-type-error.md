---
title: "[Solution] Scala Union Type Error"
description: "Fix Scala 3 union type errors when using | to combine multiple types."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Union type errors occur when union types are used incorrectly or when operations are not available on all union members.

## Common Causes

- Method not available on all union members
- Union type too broad causing type issues
- Conflicting union with intersection types
- Missing common trait for union members

## How to Fix

### 1. Use union types correctly

```scala
def process(value: Int | String): String = value match {
  case i: Int => s"Number: $i"
  case s: String => s"String: $s"
}
```

### 2. Define common interface

```scala
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Rect(w: Double, h: Double) extends Shape

def area(s: Circle | Rect): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Rect(w, h) => w * h
}
```

## Examples

```scala
type Result = Success | Failure

case class Success(value: Int)
case class Failure(error: String)

def handle(r: Result): String = r match {
  case Success(v) => s"Got: $v"
  case Failure(e) => s"Error: $e"
}

println(handle(Success(42)))
println(handle(Failure("oops")))
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Match error](/languages/scala/scala-match-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
