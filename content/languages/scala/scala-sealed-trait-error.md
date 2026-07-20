---
title: "[Solution] Scala SealedTraitError - Brief Description"
description: "Fix sealed trait exhaustiveness errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1076
---

A sealed trait error occurs when pattern matching on a sealed trait is not exhaustive.

## Common Causes

- Missing case in match for sealed trait variant
- Adding new case class without updating matches
- Non-exhaustive match on sealed hierarchy

## How to Fix

Cover all cases:

```scala
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Square(s: Double) extends Shape

def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Square(s) => s * s
}
```

Add wildcard as fallback:

```scala
def describe(s: Shape): String = s match {
  case Circle(_) => "Circle"
  case Square(_) => "Square"
  case _ => "Unknown"
}
```

## Examples

```scala
sealed trait Result
case class Success(data: String) extends Result
case class Failure(reason: String) extends Result

def handle(r: Result): String = r match {
  case Success(d) => s"Got: $d"
  case Failure(e) => s"Error: $e"
}
```

## Related Errors

- [Scala MatchError](/languages/scala/scala-match-error)
- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
