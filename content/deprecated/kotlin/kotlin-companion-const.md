---
title: "[Solution] Deprecated Function Migration: const val in companion object to top-level const"
description: "Migrate from deprecated const val in companion object to top-level constants."
deprecated_function: "companion object { const val X = 1 }"
replacement_function: "const val X = 1"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: const val in companion object to top-level const

The `companion object { const val X = 1 }` has been deprecated in favor of `const val X = 1`.

## Migration Guide

Top-level constants are simpler

const val in companion objects can be top-level constants for simplicity.

## Before (Deprecated)

```kotlin
class Constants {
    companion object {
        const val MAX_SIZE = 100
        const val DEFAULT_NAME = "user"
    }
}
```

## After (Modern)

```kotlin
// Top-level constants
const val MAX_SIZE = 100
const val DEFAULT_NAME = "user"

// Or in object
object Constants {
    const val MAX_SIZE = 100
    const val DEFAULT_NAME = "user"
}
```

## Key Differences

- Top-level constants are simpler
- No need for companion object boilerplate
- object for grouped constants
- const val for compile-time constants
