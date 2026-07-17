---
title: "[Solution] Kotlin Sealed Class When Error Fix"
description: "Fix Kotlin sealed class when expression errors. Learn why when exhaustive matching fails and how to handle sealed classes."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sealed-class", "when", "pattern-matching", "kotlin"]
weight: 5
---

## What This Error Means

A sealed class when error occurs when a when expression does not cover all possible subclasses of a sealed class. Kotlin requires exhaustive matching for sealed classes.

## Common Causes

- Missing branch in when expression
- New subclass added without updating when
- Wrong branch ordering
- Not using sealed class properly

## How to Fix

```kotlin
// WRONG: Missing branch
sealed class Result {
    object Loading : Result()
    data class Success(val data: String) : Result()
    data class Error(val message: String) : Result()
}

fun handle(result: Result) = when (result) {
    is Result.Loading -> "Loading"
    is Result.Success -> result.data
    // Missing Error branch
}

// CORRECT: Handle all branches
fun handle(result: Result) = when (result) {
    is Result.Loading -> "Loading"
    is Result.Success -> result.data
    is Result.Error -> "Error: ${result.message}"
}
```

```kotlin
// WRONG: Using else with sealed class
fun handle(result: Result) = when (result) {
    is Result.Loading -> "Loading"
    else -> "Other"  // Hides missing branches
}

// CORRECT: Let compiler enforce exhaustiveness
fun handle(result: Result) = when (result) {
    is Result.Loading -> "Loading"
    is Result.Success -> result.data
    is Result.Error -> "Error: ${result.message}"
}
```

## Examples

```kotlin
// Example 1: Basic sealed class
sealed class Shape {
    class Circle(val radius: Double) : Shape()
    class Rectangle(val width: Double, val height: Double) : Shape()
}

fun area(shape: Shape) = when (shape) {
    is Shape.Circle -> Math.PI * shape.radius * shape.radius
    is Shape.Rectangle -> shape.width * shape.height
}

// Example 2: Sealed interface
sealed interface ApiResponse {
    data class Success(val data: String) : ApiResponse
    data class Error(val code: Int) : ApiResponse
}

// Example 3: Sealed class with when as expression
val message = when (result) {
    is Result.Loading -> "Loading..."
    is Result.Success -> "Success: ${result.data}"
    is Result.Error -> "Error: ${result.message}"
}
```

## Related Errors

- [TypeCastException](typecastexception-kotlin) — type cast failed
- [ClassCastException](classcastexception-kotlin) — class cast failed
- [IllegalArgumentException](illegalargumentexception) — invalid argument
