---
title: "[Solution] Scala Package Object Error"
description: "Fix Scala package object errors when defining package-level definitions."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Package object errors occur when package objects have incorrect definitions or conflict with other package members.

## Common Causes

- Package object with name conflicting with package
- Missing package object for implicit definitions
- Package object containing non-val definitions
- Wrong syntax for package object

## How to Fix

### 1. Define package object correctly

```scala
package object mypackage {
  type StringMap[V] = Map[String, V]
  val defaultPort: Int = 8080
}
```

### 2. Use package object for shared definitions

```scala
package object utils {
  implicit val stringOrdering: Ordering[String] = Ordering.String
  def currentTime: Long = System.currentTimeMillis()
}
```

## Examples

```scala
// In file: src/mypackage/package.scala
package object mypackage {
  type Result[T] = Either[String, T]
  val MaxRetries: Int = 3
}

// In file: src/mypackage/Main.scala
package mypackage

object Main extends App {
  val r: Result[Int] = Right(42)
  println(s"Max retries: $MaxRetries")
}
```

## Related Errors

- [Import error](/languages/scala/scala-import-selector-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
