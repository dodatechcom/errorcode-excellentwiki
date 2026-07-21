---
title: "[Solution] Scala Givens Ambiguity Error"
description: "Fix Scala 3 given ambiguity errors when multiple given instances of the same type are in scope."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Given ambiguity errors occur when two or more given instances of the same type are available and the compiler cannot choose between them.

## Common Causes

- Multiple given instances of same type
- Given from different imports conflicting
- Given with same type but different priority
- Missing given priority resolution

## How to Fix

### 1. Use given priorities

```scala
trait LowPriorityGivens {
  given intOrdering: Ordering[Int] = Ordering.Int
}

object Givens extends LowPriorityGivens {
  given smallIntOrdering: Ordering[Int] = Ordering.by(_.toByte)
}
```

### 2. Select specific given

```scala
import Givens.given  // or specific given
```

## Examples

```scala
trait PriceStrategy {
  def calculate(price: Double): Double
}

given standardPrice: PriceStrategy with {
  def calculate(price: Double): Double = price
}

given discountPrice: PriceStrategy with {
  def calculate(price: Double): Double = price * 0.9
}

// Select specific given
def processStandard(price: Double)(using p: PriceStrategy = standardPrice): Double = {
  p.calculate(price)
}
```

## Related Errors

- [Implicit ambiguity error](/languages/scala/scala-implicits-ambiguity)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
