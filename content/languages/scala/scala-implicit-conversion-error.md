---
title: "[Solution] Scala ImplicitConversionError - Brief Description"
description: "Fix implicit conversion conflicts."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1072
---

An implicit conversion error occurs when multiple conversions overlap.

## Common Causes

- Multiple conversions with overlapping source types
- Companion object and import both active
- Wrong conversion applied

## How to Fix

Use extension methods instead:

```scala
implicit class IntOps(val n: Int) extends AnyVal {
  def isPositive: Boolean = n > 0
  def times(f: => Unit): Unit = (1 to n).foreach(_ => f)
}
42.isPositive
```

## Examples

```scala
implicit def stringToInt(s: String): Int = s.toInt
def double(n: Int): Int = n * 2
double("42")
```

## Related Errors

- [Scala ImplicitNotFound](/languages/scala/scala-implicit-not-found)
- [Scala ImplicitAmbiguity](/languages/scala/scala-implicits-ambiguity)
