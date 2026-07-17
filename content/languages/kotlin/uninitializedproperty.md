---
title: "[Solution] Kotlin UninitializedPropertyAccessException Fix"
description: "Fix Kotlin UninitializedPropertyAccessException when lateinit properties are accessed before initialization."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An UninitializedPropertyAccessException is thrown when you access a lateinit property that has not been initialized yet. lateinit allows you to defer initialization but requires checking before use.

## Common Causes

- Accessing lateinit before assignment
- Missing initialization in constructor
- Initialization in wrong lifecycle method
- Property initialized conditionally

## How to Fix

```kotlin
// WRONG: Accessing before initialization
class User {
    lateinit var name: String
    fun greet() = println("Hello, $name")
}

val user = User()
user.greet()  // UninitializedPropertyAccessException

// CORRECT: Check if initialized
class User {
    lateinit var name: String
    fun greet() {
        if (::name.isInitialized) {
            println("Hello, $name")
        } else {
            println("Name not set")
        }
    }
}
```

```kotlin
// WRONG: lateinit in data class
data class Config(
    lateinit var host: String  // Not ideal for data classes
)

// CORRECT: Use nullable or default value
data class Config(
    var host: String = "localhost"
)
```

```kotlin
// WRONG: Conditional initialization
class Service {
    lateinit var dependency: Dependency
    fun init(useMock: Boolean) {
        if (useMock) {
            dependency = MockDependency()
        }
        // If useMock is false, dependency not initialized
    }
}

// CORRECT: Always initialize
class Service {
    lateinit var dependency: Dependency
    fun init(useMock: Boolean) {
        dependency = if (useMock) MockDependency() else RealDependency()
    }
}
```

## Examples

```kotlin
// Example 1: Safe initialization check
class MyClass {
    lateinit var value: String

    fun isInitialized() = ::value.isInitialized
}

// Example 2: Lazy initialization
class MyClass {
    val value: String by lazy { computeValue() }
}

// Example 3: Nullable alternative
class MyClass {
    var value: String? = null
    fun doWork() {
        value?.let { println(it) } ?: println("Not set")
    }
}
```

## Related Errors

- [NullPointerException](nullpointerexception-kotlin) — null access
- [IllegalStateException](illegalstateexception-kotlin) — invalid state
- [IllegalArgumentException](illegalargumentexception) — invalid argument
