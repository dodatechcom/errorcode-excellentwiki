---
title: "[Solution] Scala Type Mismatch — Found X, Required Y"
description: "Fix Scala type mismatch compile errors. Learn about expected vs actual types, generic constraints, and implicit conversions."
languages: ["scala"]
error-types: ["compile-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A "type mismatch" compile error means the compiler found a value of one type but expected a different type at that position. The error message explicitly shows both the found type and the required type, for example: "type mismatch; found: Int, required: String".

## Why It Happens

The most common cause is passing a value of the wrong type to a function or method. For example, passing an `Int` where a `String` is expected, or passing a `List[Int]` where a `Vector[Int]` is required.

Generic type constraints are another frequent source. When a method requires `A <: Ordered[A]` and you pass a type that does not extend `Ordered`, the compiler reports a type mismatch even if the base types align.

Variance issues also produce type mismatch errors. If a `List[Dog]` is expected but you have a `List[Animal]`, the invariant or contravariant nature of the type parameter prevents the assignment.

Implicit conversions that fail to apply can leave the compiler seeing the original type instead of the converted type, producing a type mismatch where you expected the conversion to happen.

Finally, returning the wrong type from a method is a common mistake. Forgetting to convert the result or accidentally returning `Unit` from a method that should return a value.

## How to Fix It

### Check the expected type signature

```scala
// Wrong — passing Int where String expected
def greet(name: String): String = s"Hello, $name"
greet(42) // type mismatch

// Correct
greet("Alice")
```

### Use explicit type annotations

```scala
val numbers: Vector[Int] = List(1, 2, 3).toVector
```

### Add implicit evidence for generic constraints

```scala
def process[T](item: T)(implicit ev: T => Ordered[T]): T = item

// Or with context bound
def process[T: Ordering](item: T): T = item
```

### Fix variance issues with type bounds

```scala
class Container[+A](val value: A)
val animals: Container[Animal] = new Container[Dog](new Dog)
```

### Ensure return types match declarations

```scala
// Wrong — returns Unit instead of Int
def compute(x: Int): Int = {
  println(x)
}

// Correct
def compute(x: Int): Int = {
  println(x)
  x * 2
}
```

## Common Mistakes

- Ignoring the specific types in error messages and guessing at fixes
- Using `Any` or `AnyRef` to silence type errors instead of fixing the root cause
- Not understanding that `List[Dog]` is not a subtype of `List[Animal]` (invariance)
- Confusing `null` with proper `Option` usage
- Forgetting that method return types must match the declared signature

## Related Pages

- [Scala Implicit Not Found](/languages/scala/scala-implicit-not-found/)
- [Scala Value Not Member](/languages/scala/scala-value-not-member/)
- [Scala Abstract Type](/languages/scala/scala-abstract-type/)
