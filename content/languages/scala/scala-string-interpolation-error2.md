---
title: "[Solution] Scala String Interpolation Error"
description: "Fix Scala string interpolation errors when using s, f, or raw interpolators."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

String interpolation errors occur when interpolators are used incorrectly or when expressions inside interpolations have errors.

## Common Causes

- Wrong interpolator for formatting
- Missing $ for variable interpolation
- Nested quotes in interpolation
- f-interpolator format string mismatch

## How to Fix

### 1. Use correct interpolator

```scala
val name = "Alice"
val age = 30

println(s"Name: $name, Age: $age")
println(f"Name: $name%s, Age: $age%d")
println(raw"Name: $name\nNo newline")
```

### 2. Handle special characters

```scala
// WRONG: Unescaped quotes
// println(s"Say "hello"")

// CORRECT: Use block interpolation
println(s"Say ${"hello"}")
```

## Examples

```scala
val pi = 3.14159
val radius = 5.0

println(f"Area: ${pi * radius * radius}%.2f")
println(s"Radius: $radius")
println(raw"Path: C:\Users\test")
```

## Related Errors

- [Syntax error](/languages/scala/scala-type-inference-error)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Type mismatch](/languages/scala/scala-type-mismatch)
