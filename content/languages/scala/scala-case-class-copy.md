---
title: "[Solution] Scala CaseClassCopyError - Brief Description"
description: "Fix Scala case class copy errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1041
---

A case class copy error occurs when using the generated `copy` method with invalid field names or types.

## Common Causes

- Using a field name that does not exist in the case class
- Passing wrong type to a field in copy
- Confusing copy with update syntax

## How to Fix

Use correct field names:

```scala
case class User(name: String, age: Int)
val user = User("Alice", 30)
user.copy(name = "Bob")
```

Chain multiple field updates:

```scala
val updated = user.copy(name = "Bob", age = user.age + 1)
```

## Examples

```scala
case class Product(id: Int, name: String, price: Double)
val product = Product(1, "Widget", 9.99)
val discounted = product.copy(price = product.price * 0.9)
```

## Related Errors

- [Scala MatchError](/languages/scala/scala-match-error)
- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
