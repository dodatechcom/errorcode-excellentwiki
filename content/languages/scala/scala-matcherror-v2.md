---
title: "[Solution] Scala MatchError No Matching Case in Pattern Match"
description: "Fix Scala MatchError when pattern match doesn't cover all cases. Learn exhaustive matching and wildcard defaults."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `scala.MatchError` occurs when a `match` expression encounters a value that none of the cases handle. The runtime throws this when the match is not exhaustive.

## Common Causes

- Non-exhaustive match on a sealed trait or enum
- Missing wildcard case `_` for default handling
- New variant added to sealed type without updating match
- Matching on a value type without anticipating all states

## How to Fix

```scala
// WRONG: Missing default case
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
}
// describe(3) throws MatchError

// CORRECT: Add wildcard default
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
```

```scala
// WRONG: Non-exhaustive sealed trait match
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Square(s: Double) extends Shape

def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
}

// CORRECT: Cover all cases
def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Square(s) => s * s
}
```

```scala
// WRONG: Collect without fallback
val mixed: List[Any] = List(1, "hello", 3.0)
val strings: List[String] = mixed.collect {
  case s: String => s
}

// CORRECT: Use collect which is already partial
// collect only applies to matching cases — this is fine
val result = mixed.collect {
  case s: String => s
  case i: Int => i.toString
}
```

## Examples

```scala
// Example 1: Compiler warning for non-exhaustive match
// Enable warnings with -Wconf:cat=match:warning
val x: Option[Int] = Some(42)
x match {
  case Some(v) => println(v)
  // Compiler warns about missing None case
}

// Example 2: Using @unchecked to suppress warnings
import scala.unchecked
def describe(n: Int): String = (n: @unchecked) match {
  case 1 => "one"
  case 2 => "two"
}

// Example 3: Pattern matching with guards
def classify(n: Int): String = n match {
  case x if x > 0 => "positive"
  case x if x < 0 => "negative"
  case 0 => "zero"
}
```

## Related Errors

- [scala-nosuchelement]({{< relref "/languages/scala/scala-nosuchelement" >}}) — key not found in Map
- [scala-classcasterror]({{< relref "/languages/scala/scala-classcasterror" >}}) — invalid type cast
- [scala-nullpointer]({{< relref "/languages/scala/scala-nullpointer" >}}) — null pointer
