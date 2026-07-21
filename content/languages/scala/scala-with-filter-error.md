---
title: "[Solution] Scala WithFilter Error"
description: "Fix Scala withFilter errors when filtering collections in for comprehensions."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
---

withFilter errors occur when the method is not defined for a collection or when it returns unexpected results.

## Common Causes

- withFilter not available on collection type
- withFilter returns WithFilter object not collection
- Using filter instead of withFilter in for comprehension
- withFilter with incorrect predicate

## How to Fix

### 1. Use withFilter correctly

```scala
val result = for {
  x <- List(1, 2, 3, 4, 5)
  if x % 2 == 0  // uses withFilter
} yield x * 2

println(result) // List(4, 8)
```

### 2. Ensure collection supports withFilter

```scala
// Most standard collections support withFilter
val filtered = List(1, 2, 3, 4, 5).withFilter(_ > 2).map(_ * 2)
println(filtered) // List(6, 8, 10)
```

## Examples

```scala
val numbers = (1 to 10).toList
val evens = for {
  n <- numbers
  if n % 2 == 0
} yield n * n

println(s"Even squares: $evens")
```

## Related Errors

- [Filter error](/languages/scala/scala-collection-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Runtime error](/languages/scala/scala-outofmemory-v2)
