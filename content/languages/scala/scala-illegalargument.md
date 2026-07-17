---
title: "[Solution] Scala IllegalArgumentException"
description: "Fix Scala IllegalArgumentException. Learn about argument validation and precondition checks in Scala."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["illegalargument", "argument", "validation", "precondition", "require"]
weight: 5
---

## What This Error Means

An `IllegalArgumentException` occurs when a method receives an argument that is valid in type but invalid in value. This is thrown explicitly via `require` or `assert` to enforce preconditions.

## Common Causes

- Invalid argument value passed to method
- Failed `require` or `assert` check
- Null passed where non-null expected
- Out-of-range numeric values

## How to Fix

Use `require` for precondition checks:

```scala
def setAge(age: Int): Unit = {
  require(age >= 0 && age <= 150, s"Invalid age: $age")
  println(s"Age set to $age")
}
```

Validate arguments explicitly:

```scala
def divide(a: Int, b: Int): Int = {
  if (b == 0) throw new IllegalArgumentException("Cannot divide by zero")
  a / b
}
```

Use pattern matching for validation:

```scala
def processColor(color: String): Unit = color match {
  case "red" | "blue" | "green" => println(s"Processing $color")
  case _ => throw new IllegalArgumentException(s"Invalid color: $color")
}
```

Use `Either` for validated results:

```scala
def validateAge(age: Int): Either[String, Int] = {
  if (age >= 0 && age <= 150) Right(age)
  else Left(s"Invalid age: $age")
}
```

## Examples

```scala
object IllegalArgumentExample extends App {
  require(10 > 20, "10 is not greater than 20")
  // java.lang.IllegalArgumentException: requirement failed: 10 is not greater than 20
}
```

## Related Errors

- [unsupportedoperation] — operation not supported
- [matcherror] — pattern match fails
