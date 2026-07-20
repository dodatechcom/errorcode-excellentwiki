---
title: "[Solution] Kotlin NoWhenBranchMatchedException: when expression must be exhaustive"
description: "Fix Kotlin sealed class when expression errors. Learn exhaustive matching, sealed interfaces, and how the compiler enforces branch coverage."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# NoWhenBranchMatchedException: when expression must be exhaustive

A `NoWhenBranchMatchedException` is thrown at runtime when a `when` expression used as an expression (not a statement) does not have a branch that matches the input and lacks an `else` branch.

## Error Message

```
kotlin.NoWhenBranchMatchedException: when expression must be exhaustive
```

## Description

Kotlin requires `when` expressions to be exhaustive when used as an expression — meaning every possible input must have a corresponding branch. For sealed classes and sealed interfaces, the compiler enforces this at compile time. However, when using `when` as a statement or when the sealed class hierarchy changes after compilation, a `NoWhenBranchMatchedException` can occur at runtime.

This error is common when a new subclass is added to a sealed class but existing `when` blocks have not been updated, or when using a type-check cast with `when`.

## Common Causes

- A new sealed class subclass added without updating all `when` branches
- Using `when` as a statement without an `else` branch on a non-sealed type
- Proguard or R8 stripping subclasses at build time
- Dynamic class loading where the compiler cannot see all subtypes
- When matching on an interface rather than a sealed class

## Solutions

### Solution 1: Add an else branch for safety

Always include an `else` branch when using `when` as a statement to handle unexpected cases gracefully.

```kotlin
sealed class NetworkResult {
    data class Success(val data: String) : NetworkResult()
    data class Error(val code: Int) : NetworkResult()
    data object Loading : NetworkResult()
}

// Without else branch — compiler warning if sealed, runtime error if not exhaustive
fun handleResult(result: NetworkResult) = when (result) {
    is NetworkResult.Success -> println("Data: ${result.data}")
    is NetworkResult.Error -> println("Error code: ${result.code}")
    is NetworkResult.Loading -> println("Loading...")
    else -> println("Unknown state") // Safety net
}
```

### Solution 2: Use sealed interfaces for compile-time safety

Use sealed interfaces with the Kotlin compiler to guarantee exhaustiveness at compile time rather than runtime.

```kotlin
sealed interface UiEvent {
    data class Click(val x: Int, val y: Int) : UiEvent
    data class Scroll(val delta: Float) : UiEvent
    data object Idle : UiEvent
}

// Compiler will error if a branch is missing
fun processEvent(event: UiEvent): String = when (event) {
    is UiEvent.Click -> "Clicked at (${event.x}, ${event.y})"
    is UiEvent.Scroll -> "Scrolled by ${event.delta}"
    is UiEvent.Idle -> "Idle"
}
```

### Solution 3: Avoid Proguard stripping sealed subclasses

Configure Proguard to keep all subclasses of your sealed classes so they are available at runtime.

```proguard
# Keep all subclasses of sealed classes
-keep class * extends kotlinx.serialization.internal.LinkedClassDescriptor {
    ** INSTANCE;
}

# Or specifically for your sealed class
-keep class com.example.MyResult$* { *; }
```

## Prevention Tips

- Always use `when` as an expression to get compile-time exhaustiveness checking
- Prefer sealed interfaces for new code — they allow multiple inheritance
- Add `else` branches in when statements as a safety net
- Test Proguard rules to ensure sealed class subclasses are preserved
- Avoid dynamic class loading with sealed types

## Related Errors

- [ClassCastException]({{< relref "/languages/kotlin/class-cast" >}}) — wrong type cast at runtime.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument passed to function.
- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — invalid state transition.
