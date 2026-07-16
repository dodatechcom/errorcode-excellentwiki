---
title: "[Solution] Scala MatchError — No Match for Value in Pattern Matching"
description: "Fix Scala MatchError. Learn why 'a value of type X was not matched' occurs and how to make pattern matches exhaustive."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["match", "pattern-matching", "matcherror", "runtime", "sealed"]
weight: 5
---

# MatchError — No Match for Value in Pattern Matching

A `MatchError` occurs when a `match` expression encounters a value that none of the cases handle. The runtime throws `scala.MatchError` with the message "a value of type X was not matched".

## Description

Scala's `match` expression is similar to a switch statement but far more powerful. However, if no case matches the input value, a `MatchError` is thrown at runtime. This typically happens when a match is not exhaustive — meaning not all possible values of a type are covered.

Common scenarios:

- **Non-exhaustive match on an enum or sealed trait** — a new variant was added but no matching case exists.
- **Matching on a value type** — the value's type or state wasn't anticipated.
- **Default case missing** — no wildcard `_` or `case _` to catch everything.
- **Pattern match on Any** — mixing types without proper handling.

## Common Causes

```scala
// Cause 1: Non-exhaustive match on a sealed trait
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Square(s: Double) extends Shape

def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Square(s) => s * s
  // Missing case: new Shape subtype added later
}

// Cause 2: Matching on an integer without default
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
  // MatchError if n is 3
}

// Cause 3: Pattern match on wrong type
def process(x: Any): String = x match {
  case s: String => s.toUpperCase
  // MatchError if x is an Int
}

// Cause 4: Missing wildcard case
val result = List(1, 2, 3).map {
  case 1 => "one"
  case 2 => "two"
  // MatchError on 3
}
```

## How to Fix

### Fix 1: Always add a wildcard default case

```scala
// Wrong
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
}

// Correct
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
```

### Fix 2: Use @unchecked for intentionally non-exhaustive matches

```scala
// Only if you're sure the match is complete
def describe(n: Int): String = (n: @unchecked) match {
  case 1 => "one"
  case 2 => "two"
}
```

### Fix 3: Make sealed traits truly exhaustive

```scala
// Wrong — missing a subtype
sealed trait Status
case object Active extends Status
case object Inactive extends Status

def label(s: Status): String = s match {
  case Active => "active"
  // No match for Inactive
}

// Correct — cover all cases
def label(s: Status): String = s match {
  case Active   => "active"
  case Inactive => "inactive"
}
```

### Fix 4: Use collect for partial functions

```scala
// Wrong — MatchError if list contains unexpected type
val mixed: List[Any] = List(1, "hello", 3.0)
val strings: List[String] = mixed.map {
  case s: String => s
}

// Correct — collect only matches, skips non-matches
val strings: List[String] = mixed.collect {
  case s: String => s
}
```

## Examples

```scala
object MatchErrorExample extends App {
  val x: Any = 42

  // This triggers: scala.MatchError: 42 (of class java.lang.Integer)
  val result = x match {
    case s: String => s
  }
}
```

## Related Errors

- [nosuchelement] — calling `.next()` on an empty iterator.
- [ClassCastException] — invalid type cast at runtime.
- [NullPointerException] — accessing a null reference.
