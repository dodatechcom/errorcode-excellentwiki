---
title: "MatchError"
description: "A MatchError occurs when a match expression encounters a value that none of the cases handle."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["match", "pattern", "matcherror", "runtime"]
weight: 5
---

## What This Error Means

A `MatchError` occurs when a `match` expression encounters a value that none of the cases handle. The runtime throws `scala.MatchError` with the message "a value of type X was not matched".

## Common Causes

- Non-exhaustive match on an enum or sealed trait
- Matching on a value type without handling all cases
- Default case missing (no wildcard `_`)
- Pattern match on Any without proper handling

## How to Fix

```scala
// WRONG: Non-exhaustive match
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
  // MatchError if n is 3
}

// CORRECT: Add wildcard case
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
```

```scala
// WRONG: Missing sealed trait cases
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Square(s: Double) extends Shape

def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Square(s) => s * s
}

// CORRECT: Cover all cases (or add default)
def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Square(s) => s * s
  case _ => 0.0
}
```

## Examples

```scala
// Example 1: Integer without default
val x = 3
x match {
  case 1 => "one"
  case 2 => "two"
}  // MatchError: 3

// Example 2: String type match
def process(x: Any): String = x match {
  case s: String => s.toUpperCase
}  // MatchError if x is Int

// Example 3: Missing collection case
List(1, 2, 3).map {
  case 1 => "one"
  case 2 => "two"
}  // MatchError on 3
```

## Related Errors

- [ClassCastException](/languages/scala/class-cast)
- [NullPointerException](/languages/scala/null-pointer6)
