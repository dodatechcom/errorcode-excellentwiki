---
title: "[Solution] Scala Enum Parameter Error"
description: "Fix Scala 3 enum case parameter errors when enum cases have constructor arguments."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Enum parameter errors occur when enum cases have incorrect parameters or when parameterized enums are used incorrectly.

## Common Causes

- Enum case with wrong parameter type
- Enum parameter not accessible
- Parameterized enum missing default
- Enum case parameter conflict with enum parameter

## How to Fix

### 1. Define parameterized enum correctly

```scala
enum Option[+T] {
  case Some(value: T)
  case None
}

val some: Option[Int] = Option.Some(42)
val none: Option[Int] = Option.None
```

### 2. Use enum parameters correctly

```scala
enum LogLevel(val priority: Int) {
  case Debug extends LogLevel(0)
  case Info extends LogLevel(1)
  case Warn extends LogLevel(2)
  case Error extends LogLevel(3)
}

val level = LogLevel.Warn
println(s"${level} has priority ${level.priority}")
```

## Examples

```scala
enum Result[+T, +E](val isSuccess: Boolean) {
  case Ok(value: T) extends Result[T, Nothing](true)
  case Err(error: E) extends Result[Nothing, E](false)
}

val success: Result[Int, String] = Result.Ok(42)
val failure: Result[Int, String] = Result.Err("failed")

println(s"Success: ${success.isSuccess}, Failure: ${failure.isSuccess}")
```

## Related Errors

- [Enum error](/languages/scala/scala-enum-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
