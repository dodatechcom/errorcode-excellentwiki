---
title: "[Solution] Scala Toplevel IIFE Error"
description: "Fix Scala 3 top-level immediately invoked function expression errors."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

Toplevel IIFE errors occur when immediately invoked functions are used at the top level without proper syntax.

## Common Causes

- Wrong IIFE syntax at top level
- IIFE with return value not captured
- IIFE causing side effects at load time
- IIFE with incorrect parentheses

## How to Fix

### 1. Use correct IIFE syntax

```scala
val result = {
  def compute(): Int = 42
  compute()
}()
```

### 2. Use @main instead of IIFE

```scala
@main def run() = {
  println("Hello from main")
}
```

## Examples

```scala
val config = {
  val props = new java.util.Properties()
  props.setProperty("app.name", "MyApp")
  props
}()

println(s"App name: ${config.getProperty("app.name")}")
```

## Related Errors

- [Syntax error](/languages/scala/scala-type-inference-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Top level error](/languages/scala/scala-top-level-error)
