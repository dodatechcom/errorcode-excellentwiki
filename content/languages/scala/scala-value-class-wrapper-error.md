---
title: "[Solution] Scala Value Class Wrapper Error"
description: "Fix Scala value class errors when wrapping types for type safety without runtime overhead."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Value class errors occur when value classes have invalid constructors, multiple fields, or are used incorrectly.

## Common Causes

- Value class with more than one val parameter
- Value class extending another value class
- Value class with specialized type parameters
- Unboxing issues with value classes

## How to Fix

### 1. Use single val parameter

```scala
class Meter(val value: Double) extends AnyVal {
  def +(other: Meter): Meter = new Meter(value + other.value)
}

val a = new Meter(1.0)
val b = new Meter(2.0)
println((a + b).value)
```

### 2. Avoid value class pitfalls

```scala
// WRONG: Value class with multiple fields
// class Bad(val a: Int, val b: String) extends AnyVal  // compile error

// CORRECT: Single field only
class UserId(val id: Long) extends AnyVal
```

## Examples

```scala
class Dollar(val cents: Int) extends AnyVal {
  def +(other: Dollar): Dollar = new Dollar(cents + other.cents)
  def *(times: Int): Dollar = new Dollar(cents * times)
  override def toString: String = f"$$${cents / 100.0}%.2f"
}

val price = new Dollar(1999)
val total = price * 3
println(s"Total: $total")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Class cast error](/languages/scala/scala-classcast-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
