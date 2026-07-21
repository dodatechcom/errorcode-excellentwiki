---
title: "[Solution] Scala Self Type Error"
description: "Fix Scala self-type annotation errors when defining abstract dependencies in traits."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Self-type errors occur when self-type annotations are incorrect or when the required type is not mixed in.

## Common Causes

- Self-type pointing to non-existent type
- Missing required mixin for self-type
- Circular self-type dependencies
- Self-type with wrong name

## How to Fix

### 1. Use correct self-type syntax

```scala
trait Database {
  def query(sql: String): List[Map[String, Any]]
}

trait UserRepository {
  self: Database =>  // requires Database
  def findUser(id: Int): Option[String] = {
    query(s"SELECT * FROM users WHERE id=$id").headOption.map(_.toString)
  }
}
```

### 2. Ensure required traits are mixed in

```scala
class MyRepo extends UserRepository with Database {
  def query(sql: String): List[Map[String, Any]] = List.empty
}
```

## Examples

```scala
trait Logger {
  def log(msg: String): Unit
}

trait Service {
  self: Logger =>
  def process(data: String): Unit = {
    log(s"Processing: $data")
  }
}

class MyService extends Service with Logger {
  def log(msg: String): Unit = println(s"LOG: $msg")
}

val svc = new MyService()
svc.process("test data")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Trait parameter error](/languages/scala/scala-trait-parameter-error)
