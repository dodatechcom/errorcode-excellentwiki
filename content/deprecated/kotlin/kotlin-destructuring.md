---
title: "[Solution] Deprecated Function Migration: manual extraction to destructuring"
description: "Migrate from deprecated manual property extraction to destructuring."
deprecated_function: "val x = pair.first; val y = pair.second"
replacement_function: "val (x, y) = pair"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: manual extraction to destructuring

The `val x = pair.first; val y = pair.second` has been deprecated in favor of `val (x, y) = pair`.

## Migration Guide

Destructuring is concise for multiple returns

Manual extraction is verbose.

## Before (Deprecated)

```kotlin
val pair = Pair(1, "hello")
val first = pair.first
val second = pair.second
```

## After (Modern)

```kotlin
val pair = Pair(1, "hello")
val (first, second) = pair

// With data classes
data class User(val name: String, val age: Int)
val (name, age) = User("Alice", 30)
```

## Key Differences

- Destructuring extracts multiple values
- Works with Pair, Triple, data classes
