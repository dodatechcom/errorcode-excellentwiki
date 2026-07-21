---
title: "[Solution] Scala Derives Clause Error"
description: "Fix Scala 3 derives clause errors when auto-deriving type class instances."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Derives clause errors occur when the derives keyword is used incorrectly or when the type class cannot be automatically derived.

## Common Causes

- Deriving clause with non-existent type class
- Wrong syntax for derives
- Deriving conflicting instances
- Missing CanEqual/Eql for derives

## How to Fix

### 1. Use correct derives syntax

```scala
case class Point(x: Int, y: Int) derives Eq, Ord, Show
```

### 2. Ensure type class supports derivation

```scala
trait Show[T]:
  def show(t: T): String

case class Name(first: String, last: String) derives Show

given [T](using s: Show[T]): Show[List[T]] with
  def show(list: List[T]): String = list.map(s.show).mkString("[", ", ", "]")
```

## Examples

```scala
enum Color derives Eq, Ord:
  case Red, Green, Blue

val colors = List(Color.Blue, Color.Red, Color.Green)
println(s"Sorted: ${colors.sorted}")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Implicit not found error](/languages/scala/scala-implicit-not-found)
- [Compilation error](/languages/scala/scala-type-inference-error)
