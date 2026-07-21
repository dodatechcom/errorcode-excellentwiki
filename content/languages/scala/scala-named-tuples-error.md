---
title: "[Solution] Scala Named Tuples Error"
description: "Fix Scala 3 named tuple errors when creating tuples with named elements."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Named tuple errors occur when named tuples have incorrect syntax or when named elements are accessed incorrectly.

## Common Causes

- Wrong syntax for named tuple creation
- Named tuple element access using wrong syntax
- Named tuples not supported in older Scala
- Named tuple with duplicate names

## How to Fix

### 1. Use correct named tuple syntax

```scala
val point = (x = 1.0, y = 2.0)
println(point.x)  // 1.0
println(point.y)  // 2.0
```

### 2. Access named elements by name

```scala
val person = (name = "Alice", age = 30)
println(s"Name: ${person.name}, Age: ${person.age}")
```

## Examples

```scala
val color = (r = 255, g = 128, b = 0)
println(s"Color: (${color.r}, ${color.g}, ${color.b})")

val entry = (key = "version", value = "1.0")
println(s"${entry.key}: ${entry.value}")
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)
