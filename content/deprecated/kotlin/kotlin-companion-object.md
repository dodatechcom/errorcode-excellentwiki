---
title: "[Solution] Deprecated Function Migration: companion object factory to top-level functions"
description: "Migrate from deprecated companion object factories to top-level functions."
deprecated_function: "Companion object { fun create() }"
replacement_function: "Top-level function"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: companion object factory to top-level functions

The `Companion object { fun create() }` has been deprecated in favor of `Top-level function`.

## Migration Guide

Top-level functions are simpler for utility functions

Companion objects with factory methods can be replaced with simpler top-level functions.

## Before (Deprecated)

```kotlin
class User private constructor(name: String) {
    companion object {
        fun create(name: String): User {
            return User(name)
        }
    }
}
```

## After (Modern)

```kotlin
// Top-level function
fun createUser(name: String): User {
    return User(name)
}

// Or use named constructor
fun User(name: String) = UserImpl(name)
```

## Key Differences

- Top-level functions are simpler
- No need for companion object boilerplate
- Named functions for clarity
- Use companion for true static members
