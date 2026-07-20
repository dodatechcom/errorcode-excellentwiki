---
title: "[Solution] Scala ScalaTestError - Brief Description"
description: "Fix ScalaTest suite errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1069
---

A ScalaTest error occurs when test suites have incorrect syntax or assertions fail.

## Common Causes

- Using wrong test style class
- Assertion syntax errors
- Missing matcher imports

## How to Fix

Use correct test style:

```scala
import org.scalatest.funsuite.AnyFunSuite
class MySuite extends AnyFunSuite {
  test("addition") { assert(1 + 1 === 2) }
}
```

Use matchers:

```scala
import org.scalatest.matchers.should.Matchers._
class MySpec extends AnyFunSuite {
  test("string ops") { "hello".length should be(5) }
}
```

## Examples

```scala
class CalculatorTest extends AnyFunSuite {
  test("multiply") { assert(Calculator.multiply(3, 4) === 12) }
}
```

## Related Errors

- [Scala Specs2Error](/languages/scala/scala-specs2-error)
- [Scala ScalacheckError](/languages/scala/scala-scalacheck-error)
