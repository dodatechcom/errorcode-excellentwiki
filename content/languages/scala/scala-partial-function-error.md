---
title: "[Solution] Scala PartialFunctionError - Brief Description"
description: "Fix partial function errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1079
---

A partial function error occurs when a PartialFunction is used where a total function is expected.

## Common Causes

- Using `apply` on PartialFunction with unhandled input
- Confusing PartialFunction with Function1
- Using `andThen`/`orElse` incorrectly

## How to Fix

Check isDefinedAt first:

```scala
val pf: PartialFunction[Int, String] = {
  case x if x > 0 => "positive"
}

if (pf.isDefinedAt(42)) pf(42) else "not handled"
```

Use `lift` for safe access:

```scala
val result: Option[String] = pf.lift(42)
```

Compose partial functions:

```scala
val positive: PartialFunction[Int, String] = { case x if x > 0 => "positive" }
val negative: PartialFunction[Int, String] = { case x if x < 0 => "negative" }
val combined = positive orElse negative
```

## Examples

```scala
val sqrt: PartialFunction[Double, Double] = {
  case x if x >= 0 => math.sqrt(x)
}

List(4.0, -1.0, 9.0).collect(sqrt)
```

## Related Errors

- [Scala MatchError](/languages/scala/scala-match-error)
- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
