---
title: "[Solution] Scala Specs2Error - Brief Description"
description: "Fix Specs2 test errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1068
---

A Specs2 error occurs when specification syntax is incorrect or matchers fail.

## Common Causes

- Incorrect specification class hierarchy
- Matcher syntax errors
- Missing implicit conversions

## How to Fix

Use correct style:

```scala
import org.specs2.mutable._
class MySpec extends Specification {
  "My feature" should {
    "work correctly" in {
      1 + 1 must equalTo(2)
    }
  }
}
```

## Examples

```scala
import org.specs2.mutable._
class CalculatorSpec extends Specification {
  "Calculator" should {
    "add numbers" in { Calculator.add(2, 3) must equalTo(5) }
  }
}
```

## Related Errors

- [Scala ScalaTestError](/languages/scala/scala-scalatest-error)
- [Scala ScalacheckError](/languages/scala/scala-scalacheck-error)
