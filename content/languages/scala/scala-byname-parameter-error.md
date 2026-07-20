---
title: "[Solution] Scala ByNameParameterError - Brief Description"
description: "Fix by-name parameter errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1077
---

A by-name parameter error occurs when lazy evaluation semantics are misunderstood.

## Common Causes

- Evaluating by-name parameter multiple times
- Using by-name where by-value is needed
- Capturing mutable state in by-name

## How to Fix

Use by-name for lazy evaluation:

```scala
def retry[T](maxAttempts: Int)(block: => T): T = {
  var lastException: Exception = null
  for (_ <- 1 to maxAttempts) {
    try { return block } catch { case e: Exception => lastException = e }
  }
  throw lastException
}
```

Understand evaluation timing:

```scala
def log[T](msg: => T): T = {
  println(s"Evaluating: $msg")
  msg
}
```

## Examples

```scala
def when[T](condition: Boolean, block: => T): Option[T] = {
  if (condition) Some(block) else None
}

when(true, { println("side effect"); 42 })
```

## Related Errors

- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
- [Scala ImplicitNotFound](/languages/scala/scala-implicit-not-found)
