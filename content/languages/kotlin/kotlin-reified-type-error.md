---
title: "[Solution] Kotlin Reified Type Parameter in Inline Function — Type Erasure"
description: "Fix Kotlin reified type parameter errors. Learn how reified types work, their limitations, and correct usage in inline functions."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1036
---

## What This Error Means

Reified type parameters allow access to type information at runtime in inline functions, bypassing type erasure. Errors occur when `reified` is used in non-inline functions, or when the type is used in invalid runtime contexts.

## Common Causes

- Using `reified` in a non-inline function
- Attempting to use reified type to create instances with `T()`
- Reified type used in a function passed as a lambda (not inline)
- Mixing reified and non-reified type parameters

```kotlin
// ERROR: reified in non-inline function
fun <T> filter(items: List<Any>): List<T> {
    return items.filterIsInstance<T>()  // T is erased
}
```

## How to Fix

**1. Mark function as inline with reified type**

```kotlin
// CORRECT: inline + reified
inline fun <reified T> List<Any>.filterType(): List<T> {
    return filterIsInstance<T>()
}
```

**2. Use reified for type checks and casts**

```kotlin
inline fun <reified T : Any> Any.isType(): Boolean = this is T

inline fun <reified T : Any> Any.castTo(): T = this as T
```

**3. Use reified for intent extras and arguments**

```kotlin
inline fun <reified T : Parcelable> Intent.parcelable(key: String): T? {
    return if (Build.VERSION.SDK_INT >= 33) {
        getParcelableExtra(key, T::class.java)
    } else {
        @Suppress("DEPRECATION")
        getParcelableExtra(key) as? T
    }
}
```

**4. Combine with companion object factory**

```kotlin
inline fun <reified T : Entity> createEntity(id: Long): T {
    return when (T::class) {
        User::class -> User(id) as T
        Product::class -> Product(id) as T
        else -> throw IllegalArgumentException("Unknown type")
    }
}
```

## Examples

```kotlin
// Example 1: JSON deserialization with reified
inline fun <reified T : Any> Json.decodeFromString(json: String): T {
    return Json.decodeFromString(serializersModule.serializer<T>(), json)
}

// Example 2: Safe cast with reified
inline fun <reified T> Any?.safeCast(): T? = this as? T

val name: String? = someValue.safeCast<String>()

// Example 3: Reflection with reified
inline fun <reified T : Any> printTypeParams() {
    println("Type: ${T::class.simpleName}")
    println("Superclasses: ${T::class.superclasses.map { it.simpleName }}")
}

// Example 4: Service locator pattern
inline fun <reified T : Service> ServiceLocator.get(): T {
    return get(T::class.java) as T
}
```

## Related Errors

- [Inline function error](kotlin-inline-function-error) — inline issues
- [Inline value class](kotlin-inline-value-class) — value class boxing
- [Type mismatch](type-mismatch) — type conflict
