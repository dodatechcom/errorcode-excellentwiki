---
title: "[Solution] Scala Type Mismatch Error"
description: "Fix Scala type mismatch errors when the compiler finds incompatible types. Learn about type inference, variance, and generic constraints."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `type mismatch` error occurs when the Scala compiler infers or expects a different type than what is provided. This is a compile-time error that catches type safety violations.

## Common Causes

- Passing wrong type to function parameter
- Incompatible collection types
- Incorrect generic type parameters
- Variance issues (covariant/contravariant)
- Missing type annotations when inference fails

## How to Fix

```scala
// WRONG: Wrong type passed to function
def greet(name: String): String = s"Hello, $name"
greet(42)  // Type mismatch: Int expected String

// CORRECT: Convert to correct type
greet(42.toString)
// Or: greet(s"Number $42")
```

```scala
// WRONG: Incompatible collection types
val nums: List[Int] = List(1, 2, 3)
val strs: List[String] = nums  // Type mismatch: List[Int] vs List[String]

// CORRECT: Convert elements
val strs: List[String] = nums.map(_.toString)
```

```scala
// WRONG: Wrong variance
class Producer[+A] {
  def produce(a: A): Unit = {}  // Error: contravariant in covariant position
}

// CORRECT: Use correct variance annotation
class Producer[A] {
  def produce(a: A): Unit = {}
}
// Or use a separate type parameter
class Producer[+A] {
  def produce[B >: A](a: B): Unit = {}
}
```

```scala
// WRONG: Missing type annotation
val x = if (true) 42 else "hello"  // Inferred as Any

// CORRECT: Be explicit
val x: Any = if (true) 42 else "hello"
// Or ensure both branches return same type
val x: String = if (true) "yes" else "no"
```

## Examples

```scala
// Example 1: Type inference in complex expressions
def combine[A](a: A, b: A): List[A] = List(a, b)
combine(1, 2)           // List[Int]
combine("a", "b")       // List[String]

// Example 2: Implicit conversion for type matching
implicit def intToString(i: Int): String = i.toString
def printLength(s: String): Unit = println(s.length)
printLength(42)  // Works with implicit conversion

// Example 3: Generic constraints
def max[T](a: T, b: T)(implicit ord: Ordering[T]): T =
  if (ord.gteq(a, b)) a else b
max(3, 5)       // 5
max("a", "z")   // z
```

## Related Errors

- [scala-matcherror]({{< relref "/languages/scala/scala-matcherror" >}}) — pattern match failed
- [scala-classcasterror]({{< relref "/languages/scala/scala-classcasterror" >}}) — class cast error
- [scala-implicit-not-found]({{< relref "/languages/scala/scala-implicit-not-found" >}}) — implicit not found
