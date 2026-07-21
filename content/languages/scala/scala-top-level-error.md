---
title: "[Solution] Scala Top-Level Definition Error"
description: "Fix Scala 3 top-level definition errors when defining val, def, or type at package level."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Top-level definition errors occur when top-level definitions have conflicts or are used in packages that don't support them.

## Common Causes

- Name conflict between top-level definitions
- Top-level def not accessible from other files
- Top-level val initialized at wrong time
- Top-level type conflicting with class names

## How to Fix

### 1. Use unique names for top-level definitions

```scala
// file: utils.scala
def greet(name: String): String = s"Hello, $name"
val appVersion: String = "1.0.0"
```

### 2. Avoid conflicts with other definitions

```scala
// WRONG: Conflict with built-in
// val List = ...

// CORRECT: Unique names
val myList = List(1, 2, 3)
```

## Examples

```scala
// top_level.scala
package myapp

val APP_NAME = "MyApplication"
def log(msg: String): Unit = println(s"[$APP_NAME] $msg")

object Main extends App {
  log("Starting application")
}
```

## Related Errors

- [Name collision error](/languages/scala/scala-type-inference-error)
- [Import error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
