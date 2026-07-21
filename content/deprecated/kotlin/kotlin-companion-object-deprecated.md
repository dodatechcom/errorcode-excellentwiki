---
title: "[Solution] Deprecated Function Migration: companion object to top-level functions"
description: "Migrate from deprecated companion object to top-level functions."
deprecated_function: "companion object { fun create() = User() }"
replacement_function: "fun createUser() = User()"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: companion object to top-level functions

The `companion object { fun create() = User() }` has been deprecated in favor of `fun createUser() = User()`.

## Migration Guide

Top-level functions are simpler.

## Before (Deprecated)

```kotlin
class User {
    companion object {
        fun create() = User()
    }
}
```

## After (Modern)

```kotlin
fun createUser() = User()
```

## Key Differences

- Top-level functions are simpler
