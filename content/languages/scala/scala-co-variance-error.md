---
title: "[Solution] Scala CoVarianceError - Brief Description"
description: "Fix Scala covariance errors."
languages: ["scala"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1050
---

A covariance error occurs when using `+T` in a position requiring invariance.

## Common Causes

- Defining mutable field in covariant type parameter
- Method parameter position with covariant type

## How to Fix

Mark type parameters correctly:

```scala
class ImmutableList[+T](val head: T, val tail: ImmutableList[T])
```

Use lower bounds:

```scala
class Producer[+T](val items: List[T]) {
  def prepend[U >: T](item: U): Producer[U] = new Producer(item :: items)
}
```

## Examples

```scala
class Animal
class Dog extends Animal
class Box[+A](val content: A)
val dogBox: Box[Dog] = new Box(new Dog)
val animalBox: Box[Animal] = dogBox
```

## Related Errors

- [Scala ContravarianceError](/languages/scala/scala-contravariance-error)
- [Scala VarianceError](/languages/scala/scala-variance-error)
