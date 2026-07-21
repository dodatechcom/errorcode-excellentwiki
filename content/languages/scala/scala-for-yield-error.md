---
title: "[Solution] Scala For Comprehension Yield Error"
description: "Fix Scala for comprehension yield errors when using yield to collect results."
languages: ["scala"]
error-types: ["syntax-error"]
severities: ["error"]
---

For comprehension yield errors occur when yield is misplaced or when the comprehension produces wrong types.

## Common Causes

- Yield on last expression only
- Yield in wrong position
- For comprehension without yield returns Unit
- Nested for loops with wrong yield placement

## How to Fix

### 1. Place yield correctly

```scala
val result = for {
  x <- List(1, 2, 3)
  y <- List(10, 20)
} yield x * y

println(result) // List(10, 20, 20, 40, 30, 60)
```

### 2. Use yield to collect values

```scala
// WRONG: No yield returns Unit
for (x <- list) process(x)

// CORRECT: Use yield for results
val results = for (x <- list) yield process(x)
```

## Examples

```scala
val names = List("Alice", "Bob", "Charlie")
val upper = for {
  name <- names
  if name.length > 3
} yield name.toUpperCase

println(upper) // List(ALICE, CHARLIE)
```

## Related Errors

- [Match error](/languages/scala/scala-match-error)
- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
