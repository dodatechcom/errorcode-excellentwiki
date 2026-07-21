---
title: "[Solution] Scala Requires Clause Error"
description: "Fix Scala 3 require clause errors when adding constraints to class or method definitions."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Require clause errors occur when require clauses have incorrect syntax or when the constraint cannot be satisfied.

## Common Causes

- Wrong require syntax
- Require constraint always false
- Missing require for constrained type
- Require clause with wrong type parameter

## How to Fix

### 1. Use correct require syntax

```scala
class SortedList[T](using ord: Ordering[T]):
  require(ord != null)
  private var items = List.empty[T]
```

### 2. Ensure constraint is satisfiable

```scala
def process[T](list: List[T])(using ord: Ordering[T]): List[T] =
  require(list.nonEmpty)
  list.sorted
```

## Examples

```scala
class Positive private (val value: Int):
  require(value > 0, "Value must be positive")

object Positive:
  def apply(n: Int): Option[Positive] =
    if n > 0 then Some(new Positive(n))
    else None

Positive(5) match
  case Some(p) => println(s"Positive: ${p.value}")
  case None => println("Invalid")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Runtime error](/languages/scala/scala-illegalargument)
