---
title: "[Solution] Scala CompoundTypeError - Brief Description"
description: "Fix Scala compound type errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1047
---

A compound type error occurs when intersection types have conflicting members.

## Common Causes

- Conflicting method signatures
- Missing implementation for abstract members

## How to Fix

Resolve conflicting members:

```scala
trait A { def aX: Int }
trait B { def bX: String }
type AB = A with B
```

Refine types correctly:

```scala
trait Container {
  type T
  def value: T
}
val refined = new Container {
  type T = String
  def value: String = "hello"
}
```

## Examples

```scala
trait Readable { def read(): String }
trait Writable { def write(data: String): Unit }
def process(resource: Readable with Writable): Unit = {
  val data = resource.read()
  resource.write(data.toUpperCase)
}
```

## Related Errors

- [Scala StructuralTypeError](/languages/scala/scala-structural-type-error)
- [Scala SelfTypeError](/languages/scala/scala-self-type-error)
