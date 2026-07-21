---
title: "[Solution] Deprecated Function Migration: manual copying to data class copy()"
description: "Migrate from deprecated manual property copying to data class copy() in Kotlin."
deprecated_function: "Manual property copying"
replacement_function: "data class copy()"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: manual copying to data class copy()

The `Manual property copying` has been deprecated in favor of `data class copy()`.

## Migration Guide

Data classes automatically generate a copy() method for creating modified copies.

## Before (Deprecated)

```kotlin
data class User(val name: String, val age: Int, val email: String)

fun updateUser(user: User, newAge: Int): User {
    return User(user.name, newAge, user.email)
}
```

## After (Modern)

```kotlin
data class User(val name: String, val age: Int, val email: String)

fun updateUser(user: User, newAge: Int): User {
    return user.copy(age = newAge)
}

val updated = user.copy(age = 31, email = "new@example.com")
```

## Key Differences

- copy() creates shallow copy with changes
- Only named parameters need specification
- Original is not mutated
- Works with any data class
