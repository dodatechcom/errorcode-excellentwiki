---
title: "[Solution] Scala Contravariance Type Mismatch — How to Fix"
description: "Fix Scala contravariance type mismatch errors. Learn how variance annotations affect type compatibility and how to resolve compile-time conflicts."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Scala enforces variance rules on generic types to ensure type safety. A contravariance annotation (`-T`) means that a type consuming `T` can accept supertypes of `T`. When you try to use a type in a way that violates these rules, the compiler raises a type mismatch error.

The most common cause is trying to assign a `Producer[Dog]` where a `Producer[Animal]` is expected when `Producer` is contravariant in its type parameter. Because a contravariant producer accepts wider types, you cannot narrow the type parameter.

Another frequent cause is mixing covariance and contravariance in function types. Functions in Scala are contravariant in their input type and covariant in their output type. Violating this by, for example, returning a narrower type from a function where a wider type is expected, triggers the error.

Incorrect variance annotations on class definitions are a root cause. If you declare a class as covariant (`+T`) but use `T` in a position where it should be contravariant (like a method parameter), the compiler rejects the definition.

Mutable fields inside generic classes also interact with variance. A `var` in a covariant position is effectively both covariant and contravariant (invariant), and Scala does not allow variance annotations on such classes.

Finally, abstract type members with variance mismatches in trait hierarchies can produce these errors when you try to implement or override members.

## Common Error Messages

```
Error: (line, col) type mismatch;
  found   : Producer[Dog]
  required : Producer[Animal]
```

```
Error: (line, col) covariant type T occurs in contravariant position in type T of value x
```

```
Error: (line, col) illegal invariant modification of type parameter T in class Producer
```

```
Error: (line, col) contravariant type -T occurs in covariant position in type Producer[T] of method process
```

## How to Fix It

### Understand and use correct variance annotations

```scala
// Covariant — Producer[Dog] IS a subtype of Producer[Animal]
trait Producer[+T] {
  def produce: T
}

// Contravariant — Consumer[Animal] IS a subtype of Consumer[Dog]
trait Consumer[-T] {
  def consume(item: T): Unit
}
```

### Make invariant types when variance is ambiguous

```scala
// Invariant — no subtype relationship between Box[A] and Box[B]
class Box[T](val value: T)

// Box[Dog] is NOT a subtype of Box[Animal]
val dogBox: Box[Dog] = new Box(new Dog)
val animalBox: Box[Animal] = dogBox // ERROR — fixed by making it invariant
```

### Fix variance in function types

```scala
// Functions are contravariant in input, covariant in output
// This is why A => B is a subtype of C => D when C <: A and B <: D

def process(f: Animal => String): String = f(new Dog)
// This works because Dog <: Animal, and function input is contravariant
```

### Use type projections to work around variance issues

```scala
trait Container {
  type Item
  def get: Item
}

// Type projection allows working with abstract types
def process(c: Container)(item: c.Item): Unit = ???
```

### Use phantom types or evidence to enforce invariants

```scala
sealed trait Read
sealed trait Write

class File[R] private (val path: String)

object File {
  def open(path: String): File[Read] = new File[Read](path)
}

extension [R](file: File[R]) {
  def read(using ev: R <:< Read): String = ???
}
```

## Common Scenarios

- Building a generic container class and discovering that variance annotations conflict with mutable state
- Trying to pass a specialized collection where a general collection is expected
- Working with a library that uses variance annotations differently than expected

## Prevent It

- Decide early whether a generic type should be covariant, contravariant, or invariant based on its usage
- Prefer `trait` definitions with variance annotations over `class` definitions when possible
- Write variance tests by checking that subtyping relationships hold for your generic types
