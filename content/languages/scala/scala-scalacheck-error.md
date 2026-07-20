---
title: "[Solution] Scala ScalacheckError - Brief Description"
description: "Fix ScalaCheck property test errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1067
---

A ScalaCheck error occurs when property-based tests fail or generators produce invalid data.

## Common Causes

- Property does not hold for generated cases
- Generator producing invalid values
- Missing Arbitrary instances

## How to Fix

Define clear properties:

```scala
import org.scalacheck.Prop.forAll
import org.scalacheck.Properties

object StringSpec extends Properties("String") {
  property("startsWith") = forAll { (a: String, b: String) =>
    (a + b).startsWith(a)
  }
}
```

Create custom generators:

```scala
import org.scalacheck.Gen
val genUser: Gen[User] = for {
  name <- Gen.alphaStr.suchThat(_.nonEmpty)
  age <- Gen.choose(1, 100)
} yield User(name, age)
```

## Examples

```scala
val propConcat = forAll { (xs: List[Int], ys: List[Int]) =>
  (xs ++ ys).length == xs.length + ys.length
}
```

## Related Errors

- [Scala Specs2Error](/languages/scala/scala-specs2-error)
- [Scala ScalaTestError](/languages/scala/scala-scalatest-error)
