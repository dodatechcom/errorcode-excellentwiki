---
title: "[Solution] Kotlin RuntimeException — General Runtime Error Fix"
description: "Fix Kotlin RuntimeException for unexpected runtime failures. Debug the root cause, handle specific exceptions, and add proper error handling."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtimeexception", "exception", "error", "debug"]
weight: 5
---

# RuntimeException — General Runtime Error Fix

A `RuntimeException` is the superclass of all unchecked exceptions in the JVM. In Kotlin, it's a catch-all for unexpected runtime errors that don't fall into specific exception categories.

## Description

`RuntimeException` is the parent class of many common exceptions including `NullPointerException`, `IllegalArgumentException`, `IndexOutOfBoundsException`, and others. When you see a plain `RuntimeException`, it often means an unexpected error occurred that wasn't caught by more specific handlers.

Common scenarios:

- **Unexpected null in Java interop** — generic runtime failure.
- **Uncaught specific exceptions** — fallback catch for various errors.
- **Framework errors** — Spring, Android, etc. throw RuntimeException.
- **Division by zero** — `ArithmeticException` (subclass of RuntimeException).

## Common Causes

```kotlin
// Cause 1: Unexpected null from Java code
val result: String = javaMethod()  // RuntimeException if Java returns null

// Cause 2: Division by zero
val result = 10 / 0  // ArithmeticException (subclass of RuntimeException)

// Cause 3: Number parsing failure
val num = "abc".toInt()  // NumberFormatException (subclass of RuntimeException)

// Cause 4: Unhandled state
val list = listOf(1, 2, 3)
val first = list.min()  // RuntimeException if list is empty (actually NoSuchElementException)
```

## Solutions

### Fix 1: Catch specific exceptions

```kotlin
// Wrong — catching generic RuntimeException
try {
    riskyOperation()
} catch (e: RuntimeException) {
    println("Error: ${e.message}")
}

// Correct — catch specific exceptions
try {
    riskyOperation()
} catch (e: IllegalArgumentException) {
    println("Invalid argument: ${e.message}")
} catch (e: IllegalStateException) {
    println("Invalid state: ${e.message}")
} catch (e: NumberFormatException) {
    println("Number format error: ${e.message}")
}
```

### Fix 2: Use runCatching for safe error handling

```kotlin
// Wrong
try {
    val result = riskyOperation()
    process(result)
} catch (e: RuntimeException) {
    handleError(e)
}

// Correct
val result = runCatching { riskyOperation() }
result.onSuccess { process(it) }
result.onFailure { handleError(it) }
```

### Fix 3: Validate inputs to prevent RuntimeExceptions

```kotlin
// Wrong — may throw various RuntimeExceptions
fun process(data: String): Int {
    return data.toInt() + data.length
}

// Correct — validate before operating
fun process(data: String): Int {
    val num = data.toIntOrNull() ?: throw IllegalArgumentException("Not a number: $data")
    return num + data.length
}
```

### Fix 4: Use sealed classes for error handling

```kotlin
// Wrong — generic error handling
fun divide(a: Int, b: Int): Int {
    return a / b  // ArithmeticException if b == 0
}

// Correct — explicit error types
sealed class MathResult {
    data class Success(val value: Int) : MathResult()
    data class Error(val message: String) : MathResult()
}

fun divide(a: Int, b: Int): MathResult {
    return if (b != 0) {
        MathResult.Success(a / b)
    } else {
        MathResult.Error("Division by zero")
    }
}
```

## Examples

```kotlin
fun main() {
    val operations = listOf(
        { 10 / 2 },
        { "abc".toInt() },
        { 10 / 0 }
    )

    for ((index, operation) in operations.withIndex()) {
        val result = runCatching { operation() }
        result.onSuccess { println("Operation $index: $it") }
        result.onFailure { println("Operation $index failed: ${it.message}") }
    }
}
```

## Related Errors

- [NullPointerException]({{< relref "/languages/kotlin/null-pointer" >}}) — null reference access.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument.
- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — invalid object state.
