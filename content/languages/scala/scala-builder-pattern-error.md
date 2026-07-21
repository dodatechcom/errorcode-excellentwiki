---
title: "[Solution] Scala Builder Pattern Error"
description: "Fix Scala builder pattern errors when using mutable builders for constructing immutable objects."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
---

Builder pattern errors occur when builders are not properly reset after building or when the build method is called on incomplete builders.

## Common Causes

- Builder not reset after build
- build() called before all parameters set
- Builder returned wrong type
- Mutable state in builder causing issues

## How to Fix

### 1. Reset builder after build

```scala
class StringBuilder {
  private var parts = List.empty[String]
  def add(s: String): StringBuilder = { parts = parts :+ s; this }
  def build(): String = {
    val result = parts.mkString(" ")
    parts = List.empty  // reset
    result
  }
}
```

### 2. Use type-safe builders

```scala
case class Config(host: String, port: Int)
class ConfigBuilder {
  private var host: Option[String] = None
  private var port: Option[Int] = None
  def withHost(h: String) = { host = Some(h); this }
  def withPort(p: Int) = { port = Some(p); this }
  def build() = Config(host.getOrElse("localhost"), port.getOrElse(8080))
}
```

## Examples

```scala
class QueryBuilder {
  private var table: Option[String] = None
  private var conditions = List.empty[String]

  def from(t: String) = { table = Some(t); this }
  def where(c: String) = { conditions = conditions :+ c; this }
  def build(): String = s"SELECT * FROM ${table.getOrElse("?")} WHERE ${conditions.mkString(" AND ")}"
}

val query = new QueryBuilder().from("users").where("age > 18").build()
println(query)
```

## Related Errors

- [Runtime error](/languages/scala/scala-outofmemory-v2)
- [Thread safety error](/languages/scala/scala-concurrentmodification)
- [Compilation error](/languages/scala/scala-type-mismatch)
