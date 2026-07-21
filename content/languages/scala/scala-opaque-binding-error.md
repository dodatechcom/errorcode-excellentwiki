---
title: "[Solution] Scala Opaque Type Binding Error"
description: "Fix Scala 3 opaque type binding errors when opaque type aliases are not properly bound in scope."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Opaque type binding errors occur when opaque type operations are used outside their defining scope.

## Common Causes

- Using opaque type methods outside defining object
- Opaque type leaking underlying type
- Missing extension methods for opaque type
- Opaque type with no operations

## How to Fix

### 1. Define operations within scope

```scala
opaque type Meter = Double

object Meter {
  def apply(d: Double): Meter = d
  extension (m: Meter) {
    def value: Double = m
    def +(other: Meter): Meter = m + other
  }
}

import Meter.*
val a = Meter(1.0)
val b = Meter(2.0)
println((a + b).value)
```

### 2. Keep underlying type hidden

```scala
opaque type Dollars = Double

object Dollars {
  def apply(cents: Double): Dollars = cents / 100
  extension (d: Dollars) {
    def amount: Double = d
    def *(qty: Int): Dollars = d * qty
  }
}
```

## Examples

```scala
opaque type UserId = Long

object UserId {
  def apply(id: Long): UserId = id
  extension (id: UserId) {
    def toLong: Long = id
    def isValid: Boolean = id > 0
  }
}

val user = UserId(42)
println(s"Valid: ${user.isValid}")
println(s"ID: ${user.toLong}")
```

## Related Errors

- [Opaque type error](/languages/scala/scala-opaque-type-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
