---
title: "[Solution] Deprecated Function Migration: let/run/apply to with"
description: "Migrate from deprecated let/run/apply to with."
deprecated_function: "let/run/apply"
replacement_function: "with"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: let/run/apply to with

The `let/run/apply` has been deprecated in favor of `with`.

## Migration Guide

with is for non-nullable.

## Before (Deprecated)

```kotlin
obj.let {
    it.method()
}
```

## After (Modern)

```kotlin
with(obj) {
    method()
}
```

## Key Differences

- with is for non-nullable
