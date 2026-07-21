---
title: "[Solution] Scala Opaque Type Error"
description: "Fix Scala 3 opaque type alias errors when creating type-safe abstractions."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Opaque type errors occur when opaque type aliases are not properly defined or when their underlying type leaks outside the scope.

## Common Causes

- Opaque type used outside its definition scope
- Opaque type with invalid underlying type
- Missing transparent keyword for internal visibility
- Opaque type conflicting with other types

## How to Fix

### 1. Define opaque type correctly

```scala
opaque type Meter = Double

object Meter {
  def apply(d: Double): Meter = d
  extension (m: Meter) {
    def +(other: Meter): Meter = m + other
  }
}
```

### 2. Keep underlying type hidden

```scala
opaque typeelsius = Double
opaque type Fahrenheit = Double

object Celsius {
  def apply(d: Double): Celsius = d
}
object Fahrenheit {
  def apply(d: Double): Fahrenheit = d
  extension (f: Fahrenheit) {
    def toCelsius: Celsius = Celsius((f - 32) * 5 / 9)
  }
}
```

## Examples

```scala
opaque type UserId = Long

object UserId {
  def apply(id: Long): UserId = id
  extension (id: UserId) {
    def value: Long = id
    def isValid: Boolean = id > 0
  }
}

val user = UserId(42)
println(s"Valid: ${user.isValid}")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Opaque type error](/languages/scala/scala-type-erasure-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
