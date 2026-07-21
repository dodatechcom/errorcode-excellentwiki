---
title: "[Solution] Scala Enum Companions Error"
description: "Fix Scala 3 enum companion object errors when defining methods for enum cases."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Enum companion errors occur when companion objects for enums have incorrect definitions or when case methods conflict.

## Common Causes

- Enum case with wrong companion method
- Missing companion object for enum
- Enum companion conflicting with enum cases
- Enum companion method not accessible

## How to Fix

### 1. Define enum with companion correctly

```scala
enum Direction(val degrees: Int) {
  case North extends Direction(0)
  case East extends Direction(90)
  case South extends Direction(180)
  case West extends Direction(270)
}

object Direction {
  def fromDegrees(d: Int): Option[Direction] = 
    values.find(_.degrees == d % 360)
}
```

### 2. Add methods to enum cases

```scala
enum Color(val rgb: Int) {
  case Red extends Color(0xFF0000)
  case Green extends Color(0x00FF00)
  case Blue extends Color(0x0000FF)
  
  def hex: String = f"#$rgb%06X"
}

println(Color.Red.hex) // #FF0000
```

## Examples

```scala
enum Priority(val level: Int) {
  case Low extends Priority(1)
  case Medium extends Priority(2)
  case High extends Priority(3)
}

object Priority {
  def fromLevel(n: Int): Option[Priority] =
    values.find(_.level == n)
}

val p = Priority.High
println(s"${p} (level ${p.level})")
```

## Related Errors

- [Enum error](/languages/scala/scala-enum-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
