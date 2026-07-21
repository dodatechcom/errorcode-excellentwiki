---
title: "[Solution] Deprecated Function Migration: verbose builder to apply scope function"
description: "Migrate from verbose builder pattern to apply."
deprecated_function: "obj.prop1 = a; obj.prop2 = b"
replacement_function: "obj.apply { prop1 = a; prop2 = b }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: verbose builder to apply scope function

The `obj.prop1 = a; obj.prop2 = b` has been deprecated in favor of `obj.apply { prop1 = a; prop2 = b }`.

## Migration Guide

apply reduces boilerplate for configuration

Builder patterns with repeated references are verbose.

## Before (Deprecated)

```kotlin
val button = Button()
button.text = "Click me"
button.isEnabled = true
```

## After (Modern)

```kotlin
val button = Button().apply {
    text = "Click me"
    isEnabled = true
}
```

## Key Differences

- apply uses implicit this
- Reduces repeated references
- Returns the object itself
