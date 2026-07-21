---
title: "[Solution] Scala Capture Checking Error"
description: "Fix Scala 3 capture checking errors for safe usage of captured variables in functional abstractions."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Capture checking errors occur when captured variables escape their scope or when captured references conflict with safety guarantees.

## Common Causes

- Captured mutable variable escaping scope
- Capture checking not enabled
- Using captured reference after scope ends
- Conflict between capture and capability

## How to Fix

### 1. Enable capture checking

```scala
import scala.language.captureChecking

def process[T](x: T)(using cap: Capabilty): T = x
```

### 2. Keep captures within scope

```scala
def withResource[T](f: Resource => T): T = {
  val res = new Resource
  try f(res)
  finally res.close()
}
```

## Examples

```scala
class Resource {
  private var closed = false
  def close(): Unit = closed = true
  def isClosed: Boolean = closed
}

def safeUse(): Unit = {
  val res = new Resource
  // res can only be used within this block
  println(s"Closed: ${res.isClosed}")
  res.close()
}

safeUse()
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Memory safety error](/languages/scala/scala-unsafe-cast)
