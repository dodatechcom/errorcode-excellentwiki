---
title: "[Solution] Kotlin Contracts Error Fix"
description: "Fix Kotlin contracts errors. Learn why contract declarations fail and how to use Kotlin contracts properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["contracts", "smart-cast", "effect", "kotlin"]
weight: 5
---

## What This Error Means

A Kotlin contracts error occurs when contract declarations are invalid. Contracts allow the compiler to understand the effects of functions, enabling smart casts and other optimizations.

## Common Causes

- Invalid contract syntax
- Contract does not match function behavior
- Using contracts in non-inline functions
- Wrong effect type

## How to Fix

```kotlin
// WRONG: Contract in non-inline function
fun process(value: Any?) {
    contract {
        returns() implies (value != null)  // Error: not inline
    }
}

// CORRECT: Contract in inline function
inline fun process(value: Any?, block: () -> Unit) {
    contract {
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    }
    block()
}
```

```kotlin
// WRONG: Contract does not match behavior
inline fun isNotEmpty(value: String?): Boolean {
    contract {
        returns(true) implies (value != null)  // Wrong: may return false with null
    }
    return value != null && value.isNotEmpty()
}

// CORRECT: Contract matches behavior
inline fun isNotNull(value: Any?): Boolean {
    contract {
        returns(true) implies (value != null)
    }
    return value != null
}
```

## Examples

```kotlin
// Example 1: Implies contract
inline fun requireNotNull(value: Any?): Boolean {
    contract {
        returns(true) implies (value != null)
    }
    return value != null
}

fun process(value: Any?) {
    if (requireNotNull(value)) {
        println(value.length)  // Smart cast to non-null
    }
}

// Example 2: callsInPlace contract
inline fun run(block: () -> Unit) {
    contract {
        callsInPlace(block, InvocationKind.EXACTLY_ONCE)
    }
    block()
}

fun example() {
    val x: Int
    run { x = 5 }  // Allowed due to contract
    println(x)
}

// Example 3: returns contract
inline fun <T> Result<T>.getOrNull(): T? {
    contract {
        returns(null) implies (this@getOrNull.isFailure)
    }
    return getOrNull()
}
```

## Related Errors

- [Inline class error](inline-class-error) — inline class issue
- [Inline reified error](inline-reified-error) — reified type issue
- [Expect actual error](expect-actual-error) — expect/actual mismatch
