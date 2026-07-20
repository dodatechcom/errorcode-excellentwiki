---
title: "[Solution] Scala ScaladocError - Brief Description"
description: "Fix Scaladoc generation errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1066
---

A Scaladoc error occurs when documentation generation fails.

## Common Causes

- Invalid Scaladoc syntax
- Referencing non-existent symbols
- Version mismatch

## How to Fix

Use valid syntax:

```scala
/** Calculates the sum of two numbers.
  *
  * @param a first number
  * @param b second number
  * @return the sum
  */
def add(a: Int, b: Int): Int = a + b
```

## Examples

```scala
/** A simple calculator. */
object Calculator {
  /** Adds two numbers. */
  def add(a: Int, b: Int): Int = a + b
}
```

## Related Errors

- [Scala SBTPluginError](/languages/scala/scala-sbt-plugin-error)
- [Scala WartRemoverError](/languages/scala/scala-wartremover-error)
