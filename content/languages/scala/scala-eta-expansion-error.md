---
title: "[Solution] Scala Eta Expansion Error"
description: "Fix Scala eta expansion errors when converting methods to functions."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Eta expansion errors occur when methods are not properly converted to function values.

## Common Causes

- Method not eta-expanded automatically
- Eta expansion on parameterless method
- Wrong function type from eta expansion
- Missing eta expansion in higher-order functions

## How to Fix

### 1. Use explicit eta expansion

```scala
def add(a: Int, b: Int): Int = a + b

val addFunc: (Int, Int) => Int = add _  // explicit
// or in Scala 3
val addFunc2 = add  // automatic in Scala 3
```

### 2. Pass methods as functions

```scala
val nums = List(1, 2, 3)
val doubled = nums.map(_ * 2)  // lambda
val doubled2 = nums.map(double)  // if double is defined
```

## Examples

```scala
def isPositive(n: Int): Boolean = n > 0

val positives = List(-1, 2, -3, 4).filter(isPositive)
println(s"Positives: $positives")

def square(n: Int): Int = n * n
val squares = List(1, 2, 3, 4).map(square)
println(s"Squares: $squares")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Lambda case error](/languages/scala/scala-match-error)
