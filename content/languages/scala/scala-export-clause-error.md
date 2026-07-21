---
title: "[Solution] Scala Export Clause Error"
description: "Fix Scala 3 export clause errors when forwarding member selections from other objects."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Export clause errors occur when exporting members that do not exist in the source or when export names conflict.

## Common Causes

- Exporting non-existent member
- Name conflict between exported and local members
- Exporting private members
- Wrong export syntax

## How to Fix

### 1. Export valid members only

```scala
object Utils {
  def helper(): Unit = println("helper")
  def compute(x: Int): Int = x * 2
}

class Service {
  export Utils.{helper, compute}
}
```

### 2. Use selective exports

```scala
object MathOps {
  def add(a: Int, b: Int): Int = a + b
  def multiply(a: Int, b: Int): Int = a * b
}

class Calculator {
  export MathOps.{add => plus, multiply => times}
}
```

## Examples

```scala
object Logging {
  def info(msg: String): Unit = println(s"INFO: $msg")
  def error(msg: String): Unit = println(s"ERROR: $msg")
}

class Logger {
  export Logging._
}

val log = new Logger()
log.info("Application started")
log.error("Something went wrong")
```

## Related Errors

- [Import error](/languages/scala/scala-type-mismatch)
- [Name collision error](/languages/scala/scala-type-inference-error)
- [Compilation error](/languages/scala/scala-implicit-conversion-error)
