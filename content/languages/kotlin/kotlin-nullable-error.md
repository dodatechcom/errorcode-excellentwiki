---
title: "[Solution] Kotlin NullPointerException: null cannot be cast to non-null type"
description: "Fix Kotlin nullable type errors when null cannot be cast to a non-null type. Learn safe calls, Elvis operator, let blocks, and platform type handling."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# KotlinNullPointerException: null cannot be cast to non-null type

This error occurs when Kotlin code tries to cast a null value to a non-null type, or when a platform type from Java is treated as non-nullable at runtime but is actually null.

## Error Message

```
kotlin.KotlinNullPointerException: null cannot be cast to non-null type kotlin.String
```

## Description

Kotlin's type system distinguishes between nullable and non-nullable types at compile time. However, when you use unsafe casts (`as`), the `!!` operator, or receive null from Java code, the runtime will throw a `KotlinNullPointerException`. This is particularly common when deserializing JSON, working with Java APIs, or using `lateinit` variables that were never assigned.

## Common Causes

- Using the `!!` operator on a null value
- Unsafe cast with `as` instead of safe cast `as?`
- Receiving null from Java code into a non-nullable Kotlin type
- Accessing a `lateinit var` before initialization
- Parsing external data (JSON, XML) where fields may be absent

## Solutions

### Solution 1: Use safe cast operator `as?`

Replace unsafe casts with safe casts that return null instead of throwing an exception.

```kotlin
val data: Any? = getNullableData()

// Unsafe cast — throws KotlinNullPointerException if data is null
// val name = data as String

// Safe cast — returns null if data is not a String or is null
val name = data as? String
println(name ?: "No string value")
```

### Solution 2: Use safe call and Elvis operators

Chain `?.` and `?:` to safely navigate nullable values and provide defaults.

```kotlin
data class User(val name: String?, val email: String?)

fun printUser(user: User?) {
    val displayName = user?.name ?: "Unknown"
    val displayEmail = user?.email ?: "no-email@example.com"
    println("User: $displayName, Email: $displayEmail")
}

fun main() {
    printUser(User("Alice", "alice@example.com"))
    printUser(User(null, null))
    printUser(null)
}
```

### Solution 3: Use let blocks for scoped operations

Use `let` to safely operate on non-null values only when they exist.

```kotlin
val input: String? = getUserInput()

input?.let { value ->
    val trimmed = value.trim()
    val uppercased = trimmed.uppercase()
    println("Processed: $uppercased")
} ?: println("No input provided")
```

### Solution 4: Check lateinit before use

Always check if a `lateinit` variable has been initialized before accessing it.

```kotlin
class AuthService {
    lateinit var currentUser: String

    fun greet() {
        if (::currentUser.isInitialized) {
            println("Welcome back, $currentUser")
        } else {
            println("Please log in first")
        }
    }
}
```

## Prevention Tips

- Avoid the `!!` operator — use `?.` and `?:` instead
- Prefer `as?` over `as` when the value might be null
- Annotate Java return types with `@Nullable` or `@NonNull`
- Use `checkNotNull()` or `requireNotNull()` with clear error messages when null indicates a bug
- Always check `::property.isInitialized` before using `lateinit` variables

## Related Errors

- [NullPointerException]({{< relref "/languages/kotlin/null-pointer" >}}) — general null reference error.
- [ClassCastException]({{< relref "/languages/kotlin/class-cast" >}}) — wrong type cast at runtime.
- [UninitializedPropertyAccessException]({{< relref "/languages/kotlin/uninitializedproperty" >}}) — accessing lateinit before init.
