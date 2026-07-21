---
title: "[Solution] Scala Enum Error"
description: "Fix Scala 3 enum definition errors when creating enumeration types."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Enum errors occur when enum cases have incorrect definitions or when enums are used with pattern matching incorrectly.

## Common Causes

- Enum case without proper constructor
- Using old Enumeration style instead of new enum
- Pattern matching enum with wrong case names
- Missing derives clause for common traits

## How to Fix

### 1. Define enum correctly

```scala
enum Color(val hex: String) {
  case Red extends Color("#FF0000")
  case Green extends Color("#00FF00")
  case Blue extends Color("#0000FF")
}
```

### 2. Use enum with pattern matching

```scala
def describe(c: Color): String = c match {
  case Color.Red => "Red"
  case Color.Green => "Green"
  case Color.Blue => "Blue"
}
```

## Examples

```scala
enum Direction {
  case North, South, East, West
}

def opposite(d: Direction): Direction = d match {
  case Direction.North => Direction.South
  case Direction.South => Direction.North
  case Direction.East => Direction.West
  case Direction.West => Direction.East
}

println(opposite(Direction.North))
```

## Related Errors

- [Match error](/languages/scala/scala-match-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
