---
title: "[Solution] Scala ValueClassError - Brief Description"
description: "Fix value class boxing errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1075
---

A value class error occurs when value classes are used incorrectly causing boxing.

## Common Causes

- Value class with multiple fields
- Extending non-universal traits
- Using in generic context

## How to Fix

Define correctly:

```scala
class Username(val value: String) extends AnyVal
```

With universal traits:

```scala
trait Greetable { def greet(): String }
class Greeter(val name: String) extends AnyVal with Greetable {
  def greet(): String = s"Hello, $name"
}
```

## Examples

```scala
class Meter(val value: Double) extends AnyVal
def distance(m: Meter): Double = m.value
```

## Related Errors

- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
- [Scala ClassCastException](/languages/scala/class-cast)
