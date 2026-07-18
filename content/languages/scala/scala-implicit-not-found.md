---
title: "[Solution] Scala Implicit Not Found Error — How to Fix"
description: "Fix Scala implicit not found errors quickly. Learn why the compiler cannot locate implicits and how to provide them correctly in your codebase."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

The Scala compiler relies on implicits to automatically resolve values, type classes, and conversions at compile time. When you use a construct that requires an implicit value and the compiler cannot find one in scope, it raises an "implicit not found" error.

The most common cause is simply forgetting to import or define the implicit value that a method or class requires. For example, calling `implicitly[Ordering[Int]]` without an `Ordering[Int]` in scope produces this error.

Another frequent cause is scope shadowing. If you define an implicit in a narrow scope and then reference it from a wider scope, the compiler does not see it. Implicits defined inside a method are not visible outside that method.

Implicit conversion conflicts also cause this error. When two implicit conversions are available for the same type, the compiler cannot decide which one to use and reports ambiguity rather than not found, but when only one is partially applicable, you may get a not-found error.

Type class derivation failures are a modern source of this error. With Scala 3's `deriving` mechanism, if a type does not have all the required instances for its fields, the derived instance fails.

Finally, implicit priority rules can hide an implicit you thought was available. An implicit defined in a parent trait may be overridden by one in a child trait, and if the override has a narrower type, the original may no longer be found where expected.

## Common Error Messages

```
Error: (line, col) implicit not found: implicitly[Ordering[List[String]]]
```

```
Error: could not find implicit value for parameter evidence: Ordering[A]
```

```
Error: (line, col) No implicit found for parameter ordering: Ordering[MyType]
```

```
Error: diverging implicit expansion for type Show[User] starting with method showString in object Show
```

## How to Fix It

### Import the required implicit explicitly

```scala
import scala.math.Ordering.Implicits._

val sorted = List(3, 1, 2).sorted
// Requires implicit Ordering[Int] — available from standard library
```

### Define a custom implicit for your type

```scala
case class User(name: String, age: Int)

implicit val userOrdering: Ordering[User] = Ordering.by(_.age)

val users = List(User("Alice", 30), User("Bob", 25))
val sorted = users.sorted
// sorted is List(User("Bob",25), User("Alice",30))
```

### Use given/using in Scala 3

```scala
// Scala 3
trait Show[A] {
  def show(a: A): String
}

given Show[Int] with {
  def show(a: Int): String = a.toString
}

def printItem[A](item: A)(using s: Show[A]): Unit =
  println(s.show(item))

printItem(42) // Works — given Show[Int] is found
```

### Bring implicits into scope with import

```scala
object JsonCodec {
  implicit val intCodec: JsonCodec[Int] = ???
  implicit val stringCodec: JsonCodec[String] = ???
}

import JsonCodec._
// Now all codecs are available
def encode[A](value: A)(implicit codec: JsonCodec[A]): String = ???
```

### Use summon in Scala 3 as a safer alternative to implicitly

```scala
// Scala 3 — gives better error messages
val codec = summon[JsonCodec[Int]]
```

## Common Scenarios

- Using a library method that requires a type class instance you have not imported or defined
- Refactoring code and moving implicits to a different object without updating imports
- Working with generic code where the implicit must be propagated through type parameters

## Prevent It

- Always verify that required implicits are imported before calling methods that need them
- Keep implicit definitions in companion objects so they are automatically in scope
- Use `summon` or `implicitly` in tests to verify that all required implicits exist at compile time
