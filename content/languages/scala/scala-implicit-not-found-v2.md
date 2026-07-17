---
title: "[Solution] Scala Implicit Not Found Error"
description: "Fix Scala 'implicit not found' error when the compiler cannot find required implicit values. Check imports, type parameters, and implicits scope."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `implicit not found` error occurs when the Scala compiler needs an implicit value of a specific type but cannot find one in scope. This commonly happens with typeclasses, serialization, and generic functions.

## Common Causes

- Missing import for implicit definitions
- Implicit not defined for the required type
- Wrong type parameter provided
- Implicit defined in companion object but not imported
- Ambiguous implicits

## How to Fix

```scala
// WRONG: Missing implicit
def sortByKey[K: Ordering](map: Map[K, String]): List[(K, String)] =
  map.toList.sorted  // Error: implicit not found for Ordering[(K, String)]

// CORRECT: Provide correct implicit
import scala.math.Ordering.Implicits._
def sortByKey[K: Ordering](map: Map[K, String]): List[(K, String)] =
  map.toList.sortBy(_._1)
```

```scala
// WRONG: No implicit for custom type
case class Money(amount: BigDecimal)
val amounts = List(Money(10), Money(5))
val sorted = amounts.sorted  // Error: implicit not found for Ordering[Money]

// CORRECT: Define implicit Ordering
implicit val moneyOrdering: Ordering[Money] = Ordering.by(_.amount)
val sorted = amounts.sorted  // Works
```

```scala
// WRONG: Wrong import path
import scalaz.Scalaz._  // May not bring all implicits

// CORRECT: Import specific implicits or use wildcard
import scalaz._
import Scalaz._
```

## Examples

```scala
// Example 1: Define implicit for typeclass
trait Show[T] {
  def show(t: T): String
}
object Show {
  implicit val intShow: Show[Int] = new Show[Int] {
    def show(i: Int): String = i.toString
  }
}

def printShow[T](t: T)(implicit s: Show[T]): Unit = println(s.show(t))
printShow(42)  // Works: implicit found

// Example 2: Implicit conversion
implicit def stringToInt(s: String): Int = s.length

// Example 3: Summon implicit
def summonImplicit[T](implicit ev: T): T = ev
```

## Related Errors

- [scala-type-mismatch]({{< relref "/languages/scala/scala-type-mismatch" >}}) — type mismatch
- [scala-matcherror]({{< relref "/languages/scala/scala-matcherror" >}}) — pattern match failed
- [scala-not-type]({{< relref "/languages/scala/scala-not-type" >}}) — not a type error
