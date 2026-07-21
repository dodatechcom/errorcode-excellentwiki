---
title: "[Solution] Scala Wildcard Type Error"
description: "Fix Scala wildcard type errors when using _ as type parameter for unknown or existential types."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Wildcard type errors occur when wildcard types are used incorrectly or when they cause type erasure issues.

## Common Causes

- Wildcard type in pattern match
- Wildcard type preventing proper type inference
- Using wildcard where specific type needed
- Wildcard causing type erasure warning

## How to Fix

### 1. Use wildcard types correctly

```scala
val list: List[_] = List(1, 2, 3)  // List[Any]
val any: Map[_, _] = Map("a" -> 1) // Map[String, Any]
```

### 2. Provide type when needed

```scala
// WRONG: Wildcard prevents access
val list: List[_] = List(1, 2, 3)
// list.head  // type is Any

// CORRECT: Use specific type
val list: List[Int] = List(1, 2, 3)
list.head  // type is Int
```

## Examples

```scala
def printAll(list: List[_]): Unit = {
  list.foreach(println)
}

printAll(List(1, "two", 3.0))
```

## Related Errors

- [Type erasure error](/languages/scala/scala-type-erasure-error)
- [Type mismatch](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
