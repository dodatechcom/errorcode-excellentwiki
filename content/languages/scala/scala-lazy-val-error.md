---
title: "[Solution] Scala LazyValError - Brief Description"
description: "Fix lazy val initialization errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1078
---

A lazy val error occurs when lazy initialization causes deadlocks or unexpected behavior.

## Common Causes

- Lazy val initialization deadlock in actors
- Lazy val with side effects failing
- Circular lazy val dependencies

## How to Fix

Avoid side effects in lazy val:

```scala
// WRONG: Side effect in lazy val
lazy val connection: Connection = createConnection()

// CORRECT: Wrap in Try
lazy val connection: Try[Connection] = Try(createConnection())
```

Use `lazy val` with proper synchronization:

```scala
class Service {
  private lazy val config: Config = loadConfig()
  def isReady: Boolean = config.isSuccess
}
```

## Examples

```scala
object Database {
  private lazy val pool: ConnectionPool = {
    println("Initializing pool")
    new ConnectionPool(config)
  }
  def getConnection: Connection = pool.get
}
```

## Related Errors

- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
- [Scala NullPointerError](/languages/scala/null-pointer6)
