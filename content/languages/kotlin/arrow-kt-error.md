---
title: "[Solution] Kotlin Arrow.kt Monadic Error Fix"
description: "Fix Arrow.kt monadic errors. Learn why Arrow.kt functional programming constructs fail and how to handle Either/Option properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An Arrow.kt monadic error occurs when functional programming constructs like Either, Option, or Validated fail. These types provide explicit error handling without exceptions.

## Common Causes

- Missing Arrow dependency
- Wrong Either projection
- Unhandled Left case
- Option None not checked

## How to Fix

```kotlin
// WRONG: Not handling Left case
val result: Either<Error, String> = validate("input")
val value = result.get()  // Throws if Left

// CORRECT: Handle both cases
when (result) {
    is Either.Left -> println("Error: ${result.value}")
    is Either.Right -> println("Success: ${result.value}")
}
```

```kotlin
// WRONG: Ignoring Option
val option: Option<Int> = findValue("key")
val value = option.get()  // Throws if None

// CORRECT: Handle None
option.fold(
    ifEmpty = { println("No value") },
    ifSome = { println("Value: $it") }
)
```

```kotlin
// WRONG: Not using Arrow types
fun divide(a: Int, b: Int): Int {
    if (b == 0) throw ArithmeticException()  // Exception
    return a / b
}

// CORRECT: Return Either
fun divide(a: Int, b: Int): Either<String, Int> {
    if (b == 0) return Left("Division by zero")
    return Right(a / b)
}
```

## Examples

```kotlin
// Example 1: Either usage
fun parseAge(input: String): Either<String, Int> {
    val age = input.toIntOrNull() ?: return Left("Not a number")
    if (age < 0) return Left("Age must be positive")
    return Right(age)
}

// Example 2: Option usage
val config: Option<Config> = loadConfig()
config.map { it.host }.getOrElse { "localhost" }

// Example 3: Validated for multiple errors
val result = validate(user).combine(validate(address))
```

## Related Errors

- [Exposed ORM error](exposed-error) — database error
- [kotlinx.coroutines error](kotlinx-coroutines-error) — coroutine error
- [Koin dependency injection error](koin-error) — DI error
