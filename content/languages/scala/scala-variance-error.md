---
title: "[Solution] Scala Variance Error — Covariant Type in Contravariant Position"
description: "Fix Scala variance errors with covariant and contravariant type parameters. Learn variance annotations, subtyping rules, and safe type design."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A variance error occurs when a type parameter with a variance annotation (`+` for covariant, `-` for contravariant) is used in a position that violates variance rules. The error message says "covariant type A occurs in contravariant position" or "contravariant type A occurs in covariant position".

## Why It Happens

Scala enforces variance rules to preserve type safety. A covariant type (`+A`) can appear in output positions (return types) but not in input positions (method parameters). A contravariant type (`-A`) can appear in input positions but not output positions.

The most common cause is defining a mutable field or method parameter using a covariant type. For example, a `class Container[+A](var value: A)` is invalid because `var` creates both a getter (covariant, OK) and a setter (contravariant, not OK for `+A`).

Another common cause is using a covariant type in a function parameter. If `Box[+A]` has a method `def set(item: A): Unit`, the parameter position violates the covariance rule.

Invariant types (no annotation) are always safe to use in any position, which is why `List[+A]` is covariant but `Array[A]` (which is mutable) is invariant.

## How to Fix It

### Use invariant types for mutable containers

```scala
// Wrong — covariant type in contravariant position
class Container[+A](var value: A)

// Correct — invariant type for mutable fields
class Container[A](var value: A)
```

### Move covariant types to return positions only

```scala
// Wrong
class Box[+A](val items: List[A]) {
  def addItem(item: A): Box[A] = new Box(items :+ item)
}

// Correct — use a new type parameter for input
class Box[+A](val items: List[A]) {
  def addItem[B >: A](item: B): Box[B] = new Box(items :+ item)
}
```

### Use lower type bounds for covariant type parameters

```scala
class Queue[+A] {
  def enqueue[B >: A](elem: B): Queue[B] = new Queue(this.toList :+ elem)
}
```

### Use upper type bounds for contravariant parameters

```scala
trait Printer[-A] {
  def print(value: A): Unit
}

class AnimalPrinter extends Printer[Animal] {
  def print(value: Animal): Unit = println(value.name)
}

// Dog is a subtype of Animal, so Printer[Animal] can accept Dog
val printer: Printer[Dog] = new AnimalPrinter
```

### Remove variance annotations when unsure

```scala
// Invariant — works in all positions
class Store[A] {
  var item: A = _
  def get: A = item
  def set(a: A): Unit = { item = a }
}
```

## Common Mistakes

- Adding `+` to a type parameter that appears in method parameters
- Using `var` fields in classes with covariant type parameters
- Not understanding that `Function1[-T, +R]` is contravariant in input and covariant in output
- Assuming variance only matters for class hierarchies and not for method signatures
- Forgetting that variance annotations affect all uses of the type parameter in the class

## Related Pages

- [Scala Type Mismatch](/languages/scala/scala-type-mismatch/)
- [Scala Abstract Type](/languages/scala/scala-abstract-type/)
- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)
