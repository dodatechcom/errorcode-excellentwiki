---
title: "[Solution] Deprecated Function Migration: verbose scope to let/run/apply/also/with"
description: "Migrate from verbose patterns to Kotlin scope functions."
deprecated_function: "if (x != null) { x.method() }"
replacement_function: "x?.let { it.method() }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: verbose scope to let/run/apply/also/with

The `if (x != null) { x.method() }` has been deprecated in favor of `x?.let { it.method() }`.

## Migration Guide

Scope functions reduce boilerplate

Scope functions (let, run, apply, also, with) reduce boilerplate for object operations.

## Before (Deprecated)

```kotlin
val user = getUser()
if (user != null) {
    val name = user.name
    val age = user.age
    println("$name is $age")
}
```

## After (Modern)

```kotlin
getUser()?.let { user ->
    println("${user.name} is ${user.age}")
}

// apply for configuration
val config = Config().apply {
    timeout = 30
    retries = 3
}
```

## Key Differences

- let for transformations (it)
- run for transformation + context (this)
- apply for configuration (this)
- also for side effects (it)
- with for existing object
