---
title: "[Solution] Scala Match Type Error"
description: "Fix Scala 3 match type errors when using type-level pattern matching."
languages: ["scala"]
error-types: ["type-error"]
severities: ["error"]
---

Match type errors occur when match types have incorrect patterns or when the type reduction fails.

## Common Causes

- Match type with non-exhaustive patterns
- Match type reducing to bottom type
- Missing cases in match type
- Match type with overlapping patterns

## How to Fix

### 1. Cover all cases in match type

```scala
type Elem[T] = T match {
  case List[a] => a
  case Option[a] => a
  case _ => Nothing
}

val e1: Elem[List[Int]] = 42       // Int
val e2: Elem[Option[String]] = "x" // String
```

### 2. Order patterns correctly

```scala
type IsInt[T] = T match {
  case Int => true
  case _ => false
}
```

## Examples

```scala
type Flatten[T] = T match {
  case List[_[_]] => Nothing  // nested list
  case List[a] => a
  case _ => T
}

val f: Flatten[List[Int]] = 42
println(f)
```

## Related Errors

- [Type error](/languages/scala/scala-type-mismatch)
- [Compilation error](/languages/scala/scala-type-inference-error)
- [Match error](/languages/scala/scala-match-error)
