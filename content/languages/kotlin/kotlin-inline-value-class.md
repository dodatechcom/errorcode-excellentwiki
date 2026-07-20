---
title: "[Solution] Kotlin Inline Value Class — Boxing and Unboxing"
description: "Fix Kotlin inline value class boxing and unboxing issues. Learn how value classes avoid boxing overhead and their limitations."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1037
---

## What This Error Means

Inline value classes (`@JvmInline value class`) are compiled to their underlying type to avoid boxing overhead. Boxing still occurs when used as a generic type argument, nullable type, or in certain interop scenarios.

## Common Causes

- Using value class in generic context causes boxing
- Nullable value class type `MyClass?` causes boxing
- Value class used as interface implementation causes boxing
- Collections of value classes (`List<MyValueClass>`) are boxed

```kotlin
@JvmInline
value class UserId(val id: Long)

// Boxing occurs here
val ids: List<UserId> = listOf(UserId(1), UserId(2))  // Boxed
```

## How to Fix

**1. Understand when boxing occurs**

```kotlin
@JvmInline
value class UserId(val id: Long)

// No boxing: direct usage
fun process(id: UserId) { ... }

// Boxing: generic context
fun <T> processGeneric(value: T) { ... }  // T is boxed
```

**2. Use inline collections for zero-allocation**

```kotlin
import kotlinx.collections.immutable.ImmutableList

// Still boxed — value class in List
val boxedIds: List<UserId> = listOf(UserId(1))

// Use primitive array for zero boxing
val rawIds: LongArray = longArrayOf(1L, 2L, 3L)
```

**3. Use @JvmInline with specific targets**

```kotlin
@JvmInline
value class Email(val value: String) {
    init {
        require(value.contains("@")) { "Invalid email" }
    }
}

// Used directly — no boxing
fun sendEmail(to: Email) { ... }
```

**4. Avoid boxing with function parameters**

```kotlin
// No boxing — direct Long parameter
fun processId(id: Long) { ... }

// Boxing — value class parameter in inline function
inline fun processUserId(id: UserId) { ... }  // Still inline, minimal overhead
```

## Examples

```kotlin
// Example 1: Multiple value classes for type safety
@JvmInline value class UserId(val value: Long)
@JvmInline value class OrderId(val value: Long)
@JvmInline value class ProductId(val value: Long)

// Compiler prevents mixing types
fun getUser(id: UserId) { ... }
fun getOrder(id: OrderId) { ... }

// Example 2: Value class with init validation
@JvmInline
value class Password(val value: String) {
    init {
        require(value.length >= 8) { "Password too short" }
        require(value.any { it.isUpperCase() }) { "Must contain uppercase" }
    }
}

// Example 3: Value class in data class (still boxed in data class)
data class User(
    val id: UserId,    // Boxed in data class copy/toString
    val name: String
)
```

## Related Errors

- [Inline class error](inline-class-error) — value class restrictions
- [Reified type error](kotlin-reified-type-error) — type erasure
- [Inline function error](kotlin-inline-function-error) — inline issues
