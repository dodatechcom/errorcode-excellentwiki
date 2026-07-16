---
title: "[Solution] Kotlin ClassCastException — Type Cast Failed Fix"
description: "Fix Kotlin ClassCastException when type casting fails. Learn how to use safe casts and type checks in Kotlin."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["classcastexception", "type-cast", "as", "kotlin"]
weight: 5
---

# ClassCastException — Type Cast Failed

A `ClassCastException` occurs when you attempt to cast an object to a type it doesn't belong to.

## Description

Kotlin uses `as` for explicit type casts. If the object isn't of the target type, the cast fails. Kotlin's `is` check and safe cast `as?` help prevent these errors.

Common causes:

- **Unsafe downcast** — casting to incorrect subtype
- **Java generic erasure** — runtime type information lost
- **Wrong collection type** — casting collection elements
- **Interface implementation** — casting to wrong interface

## Common Causes

```kotlin
// Cause 1: Unsafe downcast
open class Animal
class Dog : Animal()
class Cat : Animal()

val animal: Animal = Cat()
val dog = animal as Dog  // ClassCastException

// Cause 2: Java generic erasure
val list: List<Any> = listOf("a", "b", "c")
val strings = list as List<String>  // May throw ClassCastException

// Cause 3: Wrong collection type
val mixed: List<Any> = listOf(1, "two", 3.0)
val first = mixed[0] as String  // ClassCastException

// Cause 4: Interface cast
val map = HashMap<String, Int>()
val mutableMap = map as MutableMap<String, Int>  // Works, but risky
```

## How to Fix

### Fix 1: Use safe cast `as?`

```kotlin
// Wrong
val animal: Animal = Cat()
val dog = animal as Dog  // ClassCastException

// Correct
val dog = animal as? Dog
dog?.bark()  // Safe, dog is null if cast fails
```

### Fix 2: Use `is` check

```kotlin
// Wrong
val animal: Animal = Cat()
val dog = animal as Dog  // ClassCastException

// Correct
if (animal is Dog) {
    animal.bark()
}
```

### Fix 3: Use `when` for multiple types

```kotlin
// Wrong
val animal: Animal = Cat()
val dog = animal as Dog  // ClassCastException

// Correct
when (animal) {
    is Dog -> animal.bark()
    is Cat -> animal.meow()
    else -> println("Unknown animal")
}
```

### Fix 4: Filter collection elements

```kotlin
// Wrong
val mixed: List<Any> = listOf(1, "two", 3.0)
val first = mixed[0] as String  // ClassCastException

// Correct
val strings = mixed.filterIsInstance<String>()
```

## Examples

```kotlin
// Example 1: Safe casting with smart cast
fun process(value: Any) {
    when (value) {
        is String -> println("String: $value")
        is Int -> println("Int: $value")
        is Double -> println("Double: $value")
        else -> println("Unknown type")
    }
}

// Example 2: Safe collection casting
val data: List<Any> = listOf(1, "hello", 3.0)
val strings = data.filterIsInstance<String>()
val ints = data.filterIsInstance<Int>()
```

## Related Errors

- [NullPointerException]({{< relref "/languages/kotlin/nullpointer-kotlin" >}}) — null dereference
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument
- [UnsupportedOperationException]({{< relref "/languages/kotlin/unsupported-operation" >}}) — unsupported operation
