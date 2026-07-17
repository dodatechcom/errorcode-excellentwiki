---
title: "[Solution] Kotlin IllegalArgumentException Fix"
description: "Fix Kotlin IllegalArgumentException when invalid arguments are passed. Learn why argument validation fails and how to validate inputs."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An IllegalArgumentException is thrown when a method receives an inappropriate argument. This is a common way to enforce preconditions in Kotlin code.

## Common Causes

- Null passed to non-null parameter
- Value outside allowed range
- Invalid format or pattern
- Missing required argument

## How to Fix

```kotlin
// WRONG: Not validating arguments
fun setAge(age: Int) {
    if (age < 0) {
        throw IllegalArgumentException("Age must be non-negative")  // Throws
    }
}

// CORRECT: Validate and handle
fun setAge(age: Int) {
    require(age >= 0) { "Age must be non-negative" }
}
```

```kotlin
// WRONG: Ignoring require/check
fun processInput(input: String) {
    require(input.isNotEmpty()) { "Input must not be empty" }
    // May throw if empty
}

// CORRECT: Check before calling
if (input.isNotEmpty()) {
    processInput(input)
}
```

```kotlin
// WRONG: Null passed to non-null
fun greet(name: String) {
    println("Hello, $name")
}
greet(null)  // IllegalArgumentException

// CORRECT: Use nullable type
fun greet(name: String?) {
    println("Hello, ${name ?: "stranger"}")
}
```

## Examples

```kotlin
// Example 1: require function
fun divide(a: Int, b: Int): Int {
    require(b != 0) { "Division by zero" }
    return a / b
}

// Example 2: check function
fun processUser(user: User?) {
    check(user != null) { "User must not be null" }
    // user is smart-cast to User
}

// Example 3: Precondition in constructor
class PositiveNumber(val value: Int) {
    init {
        require(value > 0) { "Value must be positive" }
    }
}
```

## Related Errors

- [UnsupportedOperationException](unsupportedoperationexception) — operation not supported
- [NullPointerException](nullpointerexception-kotlin) — null access
- [NumberFormatException](numberformatexception-kotlin) — parsing failed
