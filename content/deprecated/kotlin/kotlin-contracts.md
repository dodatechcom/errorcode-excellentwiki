---
title: "[Solution] Deprecated Function Migration: smart cast workarounds to contracts"
description: "Migrate from deprecated smart cast workarounds to contracts."
deprecated_function: "manual null checks before cast"
replacement_function: "contract { returns() implies (value != null) }"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.3+"
---

# [Solution] Deprecated Function Migration: smart cast workarounds to contracts

The `manual null checks before cast` has been deprecated in favor of `contract { returns() implies (value != null) }`.

## Migration Guide

Contracts enable smart casts in lambdas.

## Before (Deprecated)

```kotlin
val result = myFunction()
if (result != null) {
    result.length
}
```

## After (Modern)

```kotlin
import kotlin.contracts.contract

fun myFunction(): String? {
    contract { returns() implies (result != null) }
    return if (condition) "hello" else null
}
```

## Key Differences

- Contracts enable smart casts
