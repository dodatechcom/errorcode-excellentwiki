---
title: "[Solution] Scala Multiversal Equality Error"
description: "Fix Scala 3 multiversal equality errors when using == and != with types that don't support comparison."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Multiversal equality errors occur when attempting to compare values of unrelated types using == or !=.

## Common Causes

- Comparing values of incompatible types
- Multiversal equality not enabled
- Using == on types without Equals
- Ambiguous equality comparison

## How to Fix

### 1. Enable multiversal equality

```scala
import scala.language.strictEquality

val a: Int = 1
val b: Int = 2
println(a == b)  // OK
```

### 2. Do not compare unrelated types

```scala
// WRONG: Cannot compare Int and String
// val result = 1 == "hello"

// CORRECT: Compare same types
val result = 1 == 2  // false
```

## Examples

```scala
import scala.language.strictEquality

case class Point(x: Int, y: Int)

val p1 = Point(1, 2)
val p2 = Point(1, 2)
println(p1 == p2)  // true

val list1 = List(1, 2, 3)
val list2 = List(1, 2, 3)
println(list1 == list2)  // true
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)
