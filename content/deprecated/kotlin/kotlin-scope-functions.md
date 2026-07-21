---
title: "[Solution] Deprecated Function Migration: verbose null checks to scope functions"
description: "Migrate from verbose patterns to Kotlin scope functions."
deprecated_function: "if (obj != null) { obj.prop = ... }"
replacement_function: "obj?.let { ... } / obj.apply { ... }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: verbose null checks to scope functions

The `if (obj != null) { obj.prop = ... }` has been deprecated in favor of `obj?.let { ... } / obj.apply { ... }`.

## Migration Guide

Scope functions reduce boilerplate

let, apply, run, also, with reduce boilerplate.

## Before (Deprecated)

```kotlin
val config = loadConfig()
if (config != null) {
    config.timeout = 30
    saveConfig(config)
}
```

## After (Modern)

```kotlin
loadConfig()?.apply {
    timeout = 30
}?.let { saveConfig(it) }
```

## Key Differences

- let for transformations
- apply for configuration
- run for transformation + context
