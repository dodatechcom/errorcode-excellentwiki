---
title: "[Solution] Deprecated Function Migration: if-let to takeIf/takeUnless"
description: "Migrate from deprecated if-let to takeIf/takeUnless."
deprecated_function: "if (x != null) x else null"
replacement_function: "x.takeIf { it != null }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: if-let to takeIf/takeUnless

The `if (x != null) x else null` has been deprecated in favor of `x.takeIf { it != null }`.

## Migration Guide

takeIf/takeUnless are more concise.

## Before (Deprecated)

```kotlin
val result = if (x != null) x else null
```

## After (Modern)

```kotlin
val result = x.takeIf { it != null }
```

## Key Differences

- takeIf/takeUnless are concise
