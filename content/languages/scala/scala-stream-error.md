---
title: "[Solution] Scala Stream Error"
description: "Fix Scala Stream errors including lazy evaluation issues and stack overflow from infinite streams."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
---

Stream errors occur when lazy streams are not properly evaluated, leading to memory issues or unexpected behavior.

## Common Causes

- Infinite stream without proper termination
- Stack overflow from deep stream evaluation
- Stream element evaluated unexpectedly
- Missing lazy evaluation with strict collections

## How to Fix

### 1. Use #:: for stream construction

```scala
val naturals: LazyList[Int] = 1 #:: naturals.map(_ + 1)
val first10 = naturals.take(10).toList
```

### 2. Avoid forcing entire stream

```scala
// WRONG: Forces entire infinite stream
val all = naturals.toList

// CORRECT: Use take or filter
val result = naturals.filter(_ % 2 == 0).take(5).toList
```

## Examples

```scala
val fibs: LazyList[BigInt] = BigInt(0) #:: BigInt(1) #:: fibs.zip(fibs.tail).map {
  case (a, b) => a + b
}

println(s"First 10 Fibonacci: ${fibs.take(10).toList}")
```

## Related Errors

- [Stack overflow error](/languages/scala/scala-stack-overflow)
- [Out of memory error](/languages/scala/scala-out-of-memory)
- [Runtime error](/languages/scala/scala-unsupportedoperation)
