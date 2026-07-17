---
title: "[Solution] Kotlin ClassCastException Fix"
description: "Fix Kotlin ClassCastException when type cast fails. Learn why casting fails and how to use safe casting operators."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["classcastexception", "type-cast", "class-cast", "kotlin"]
weight: 5
---

## What This Error Means

A ClassCastException is thrown when you try to cast an object to a type it is not. Kotlin provides safe casting with `as?` and forced casting with `as!`.

## Common Causes

- Using forced cast on wrong type
- Platform type from Java
- Generic type erasure
- Wrong collection element type

## How to Fix

```kotlin
// WRONG: Forced cast on wrong type
val value: Any = "hello"
val number = value as Int  // ClassCastException

// CORRECT: Use safe cast
val number = value as? Int  // null
```

```kotlin
// WRONG: Unsafe downcast
open class Animal
class Dog : Animal()
class Cat : Animal()

val animals: List<Animal> = listOf(Dog(), Cat())
val cat = animals[0] as Cat  // ClassCastException

// CORRECT: Safe downcast
val dog = animals[0] as? Dog  // Dog
```

```kotlin
// WRONG: Ignoring Java platform types
val javaList: List<Any?> = getJavaList()
val str = javaList[0] as String  // May be null

// CORRECT: Check type first
val str = javaList[0] as? String
```

## Examples

```kotlin
// Example 1: Basic safe casting
val value: Any = "hello"
val intVal = value as? Int  // null
val strVal = value as? String  // "hello"

// Example 2: When expression with casting
when (value) {
    is String -> println(value.length)
    is Int -> println(value + 1)
    else -> println("Unknown type")
}

// Example 3: Collection casting
val mixed: List<Any> = listOf(1, "two", 3.0)
val strings = mixed.filterIsInstance<String>()
```

## Related Errors

- [NullPointerException](nullpointerexception-kotlin) — null access
- [TypeCastException](typecastexception-kotlin) — type cast issue
- [IllegalArgumentException](illegalargumentexception) — invalid argument
