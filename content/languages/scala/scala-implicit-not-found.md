---
title: "[Solution] Scala Implicit Not Found — Missing Implicit Value for Type"
description: "Fix Scala implicit not found errors. Learn how to provide implicit values, resolve ambiguity, and debug implicit resolution chains."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

An "implicit not found" compile error occurs when the Scala compiler cannot find an implicit value of the required type to pass to a method or constructor that expects one. The error message shows the type it was looking for, such as "implicit not found: implicit evidence: scala.Ordering[A]".

## Why It Happens

The most common cause is calling a method that requires an implicit parameter without having one in scope. For example, calling `.sorted` on a `List[CustomType]` requires an implicit `Ordering[CustomType]`, which the standard library provides for basic types but not for your own types.

Another frequent cause is implicit scope confusion. When implicits are defined in companion objects, the compiler looks in the companion of each type involved. If the implicit is defined in a different package or object, it may not be found.

Ambiguity between multiple implicits of the same type also triggers this error. If two implicits in scope both match, the compiler reports ambiguity rather than choosing one.

Finally, importing implicits from the wrong scope or forgetting to import them entirely will cause this error. Cats, Shapeless, and other libraries rely heavily on implicits that must be explicitly imported.

## How to Fix It

### Define an implicit Ordering for custom types

```scala
case class Person(name: String, age: Int)

object Person {
  implicit val ordering: Ordering[Person] = Ordering.by(_.age)
}

// Now this works
val people = List(Person("Alice", 30), Person("Bob", 25))
val sorted = people.sorted
```

### Import required implicits explicitly

```scala
import scala.concurrent.ExecutionContext.Implicits.global
import cats.implicits._
import cats.syntax.all._
```

### Provide implicit values as function arguments

```scala
def mergeSort[T](list: List[T])(implicit ord: Ordering[T]): List[T] = {
  if (list.length <= 1) list
  else {
    val (left, right) = list.splitAt(list.length / 2)
    merge(mergeSort(left), mergeSort(right))
  }
}

// Call with explicit implicit
implicit val intOrdering: Ordering[Int] = Ordering.Int
mergeSort(List(3, 1, 4, 1, 5))
```

### Use context bounds for cleaner syntax

```scala
def max[T: Ordering](a: T, b: T): T =
  if (implicitly[Ordering[T]].compare(a, b) > 0) a else b
```

### Debug implicit resolution with the compiler flag

```bash
# Show implicit search details
scalac -Xlog-implicits myFile.scala
```

## Common Mistakes

- Forgetting to import `scala.concurrent.ExecutionContext.Implicits.global` for Future operations
- Not defining implicit instances in companion objects where the compiler looks first
- Mixing implicit versions between major library releases (e.g., Cats 2.x vs 3.x)
- Assuming implicit resolution works across package boundaries without explicit imports
- Creating circular implicit dependencies that cause infinite loops during compilation

## Related Pages

- [Scala Type Mismatch](/languages/scala/scala-type-mismatch/)
- [Scala Type Variance Error](/languages/scala/scala-variance-error/)
- [Scala SBT Resolution Failed](/languages/scala/scala-sbt-error/)
