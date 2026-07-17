---
title: "[Solution] Scala MatchError - Pattern Match Failed"
description: "Fix Scala MatchError. Learn why 'a value of type X was not matched' occurs and how to make pattern matches exhaustive."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["match", "pattern-matching", "matcherror", "runtime", "sealed"]
weight: 5
---

## What This Error Means

A `MatchError` occurs when a `match` expression encounters a value that none of the cases handle. The runtime throws `scala.MatchError` when the match is not exhaustive.

## Common Causes

- Non-exhaustive match on a sealed trait or enum
- Missing wildcard case `_` for default handling
- New variant added to sealed type without updating match
- Matching on a value type without anticipating all states

## How to Fix

Always add a wildcard default case:

```scala
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
```

Make sealed traits exhaustive:

```scala
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Square(s: Double) extends Shape

def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Square(s) => s * s
}
```

Use `@unchecked` for intentionally non-exhaustive matches:

```scala
def describe(n: Int): String = (n: @unchecked) match {
  case 1 => "one"
  case 2 => "two"
}
```

Use `collect` for partial functions:

```scala
val mixed: List[Any] = List(1, "hello", 3.0)
val strings: List[String] = mixed.collect {
  case s: String => s
}
```

## Examples

```scala
object MatchErrorExample extends App {
  val x: Any = 42
  val result = x match {
    case s: String => s
  }
  // MatchError: 42 (of class java.lang.Integer)
}
```

## Related Errors

- [nosuchelement] — calling `.next()` on an empty iterator
- [classcasterror] — invalid type cast at runtime
