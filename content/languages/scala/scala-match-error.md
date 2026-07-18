---
title: "[Solution] Scala MatchError — Value Not Covered by Any Case in Pattern Match"
description: "Fix Scala MatchError when a value is not covered by any case. Learn exhaustive matching, wildcard patterns, and sealed trait handling."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `MatchError` is thrown at runtime when a `match` expression encounters a value that none of the defined cases handle. The error message reads "a value of type X was not matched". This is one of the most common runtime errors in Scala because the compiler only enforces exhaustiveness for `@unchecked` annotated types and sealed hierarchies in some configurations.

## Why It Happens

The most frequent cause is a non-exhaustive pattern match on a sealed trait or an enum where a new variant was added without updating all match expressions. For example, if you define a sealed trait `Result` with `Success` and `Failure` cases, then add a `Pending` case later, every existing match on `Result` will throw `MatchError` unless it has a wildcard or covers `Pending`.

Another common cause is matching on `Int`, `String`, or other non-sealed types without a wildcard `_` case. The compiler cannot verify that all possible values are covered, so it relies on you to include a default.

Pattern matching on nested structures can also cause this error when an inner value does not match expectations. For instance, matching `Some(List(1, 2))` will fail if the list is empty or contains different elements.

Finally, using `match` inside a partial function (like `list.map { case x => ... }`) without covering all possible elements will produce a `MatchError` at runtime rather than a compile error.

## How to Fix It

### Add a wildcard default case

```scala
def describe(n: Int): String = n match {
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
```

### Make sealed traits exhaustive

```scala
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Square(s: Double) extends Shape

def area(s: Shape): Double = s match {
  case Circle(r) => math.Pi * r * r
  case Square(s) => s * s
}
```

### Use collect for partial function matching

```scala
val mixed: List[Any] = List(1, "hello", 3.0)
val strings = mixed.collect {
  case s: String => s.toUpperCase
}
```

### Use @unchecked for intentionally non-exhaustive matches

```scala
def describe(n: Int): String = (n: @unchecked) match {
  case 1 => "one"
  case 2 => "two"
}
```

### Handle nested patterns completely

```scala
def process(opt: Option[List[Int]]): String = opt match {
  case Some(Nil)        => "empty list"
  case Some(x :: _)     => s"first element: $x"
  case None             => "nothing"
}
```

## Common Mistakes

- Adding a new case class to a sealed trait without updating every match expression that uses it
- Assuming the compiler will warn about non-exhaustive matches on non-sealed types
- Using `match` in `map`/`flatMap`/`foreach` without a wildcard case
- Forgetting that `match` on `Any` requires handling all possible types
- Nesting patterns too deeply, making it easy to miss a branch

## Related Pages

- [Scala ClassCastException](/languages/scala/class-cast/)
- [Scala NoSuchElementException](/languages/scala/nosuchelement/)
- [Scala NullPointerException](/languages/scala/null-pointer6/)
