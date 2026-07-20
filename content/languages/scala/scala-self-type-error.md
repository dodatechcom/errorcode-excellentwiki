---
title: "[Solution] Scala SelfTypeError - Brief Description"
description: "Fix Scala self-type errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1045
---

A self-type error occurs when mixing in a trait with unmet self-type dependencies.

## Common Causes

- Missing required trait in mix-in chain
- Circular self-type dependencies
- Self-type not satisfied by class hierarchy

## How to Fix

Ensure all self-type dependencies are met:

```scala
trait Database {
  def query(sql: String): List[Map[String, Any]]
}
trait UserRepository {
  self: Database =>
  def findAll(): List[Map[String, Any]] = query("SELECT * FROM users")
}
class App extends UserRepository with Database {
  def query(sql: String): List[Map[String, Any]] = Nil
}
```

## Examples

```scala
trait Logger { def log(msg: String): Unit }
trait Service {
  self: Logger =>
  def execute(): Unit = { log("Executing service") }
}
```

## Related Errors

- [Scala CompoundTypeError](/languages/scala/scala-compound-type-error)
- [Scala TypeMismatch](/languages/scala/scala-type-mismatch)
