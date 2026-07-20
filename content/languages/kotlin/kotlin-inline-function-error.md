---
title: "[Solution] Kotlin Inline Function — Non-local Return and noinline/crossinline"
description: "Fix Kotlin inline function errors including non-local return and noinline/crossinline misuse. Learn correct inline function patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1029
---

## What This Error Means

Inline function errors occur when non-local returns are used in lambda parameters that don't support them, or when `noinline`/`crossinline` modifiers are incorrectly applied.

## Common Causes

- Non-local return from a lambda in an inline function (not marked `crossinline` or `noinline`)
- Using `crossinline` when non-local return is needed
- Passing inline lambda to another function without `noinline`
- Inline function capturing non-inline lambdas

```kotlin
// ERROR: Non-local return not allowed
inline fun repeat(action: () -> Unit) {
    repeat(3) { action() }
}

fun test() {
    repeat {
        return  // Non-local return — compile error without proper modifier
    }
}
```

## How to Fix

**1. Use crossinline for inline lambdas that can't return**

```kotlin
inline fun runOnBackground(crossinline action: () -> Unit) {
    thread {
        action()  // OK — crossinline prevents non-local return
    }
}
```

**2. Use noinline for lambdas passed to other functions**

```kotlin
inline fun process(noinline onComplete: () -> Unit) {
    background { onComplete() }  // noinline — lambda stored, not inlined
    foreground { onComplete() }  // noinline
}
```

**3. Use reified for type parameters**

```kotlin
inline fun <reified T> filterByType(items: List<Any>): List<T> {
    return items.filterIsInstance<T>()
}
```

**4. Understand non-local return semantics**

```kotlin
inline fun forEach(list: List<Int>, action: (Int) -> Unit) {
    for (item in list) action(item)
}

fun example() {
    forEach(listOf(1, 2, 3)) {
        if (it == 2) return  // Non-local return — exits example()
    }
}
```

## Examples

```kotlin
// Example 1: crossinline usage
inline fun <T> measureTime(crossinline block: () -> T): Pair<T, Long> {
    val start = System.nanoTime()
    val result = block()
    return result to System.nanoTime() - start
}

// Example 2: noinline for nullable lambda
inline fun optionalWork(noinline onComplete: (() -> Unit)? = null) {
    doWork()
    onComplete?.invoke()
}

// Example 3: reified type filter
inline fun <reified T : Any> List<Any>.filterType(): List<T> {
    return filterIsInstance<T>()
}

val ints = listOf(1, "hello", 2, "world").filterType<Int>()  // [1, 2]
```

## Related Errors

- [Inline class error](inline-class-error) — value class issue
- [Inline value class](kotlin-inline-value-class) — boxing/unboxing
- [Reified type error](kotlin-reified-type-error) — type erasure
