---
title: "[Solution] Scala EitherError - Brief Description"
description: "Fix Scala Either errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1054
---

An Either error occurs when using `Either` without proper pattern matching.

## Common Causes

- Confusing Left/Right convention
- Using `.left.get` without safety

## How to Fix

Use Left for errors, Right for success:

```scala
def divide(a: Int, b: Int): Either[String, Double] = {
  if (b == 0) Left("Division by zero")
  else Right(a.toDouble / b)
}
```

Use for-comprehensions:

```scala
def process(input: String): Either[String, Int] = for {
  num <- parseNumber(input)
  validated <- validateNumber(num)
} yield validated
```

## Examples

```scala
def parseAge(s: String): Either[String, Int] = {
  try {
    val age = s.toInt
    if (age >= 0) Right(age) else Left("Age cannot be negative")
  } catch {
    case _: NumberFormatException => Left("Invalid number")
  }
}
```

## Related Errors

- [Scala TryError](/languages/scala/scala-try-error)
- [Scala OptionGetError](/languages/scala/scala-option-get-error)
