---
title: "[Solution] Deprecated Function Migration: inner class alias to type alias"
description: "Migrate from deprecated inner class alias to type alias."
deprecated_function: "class MyList : ArrayList<Item>()"
replacement_function: "typealias MyList = ArrayList<Item>"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.4+"
---

# [Solution] Deprecated Function Migration: inner class alias to type alias

The `class MyList : ArrayList<Item>()` has been deprecated in favor of `typealias MyList = ArrayList<Item>`.

## Migration Guide

typealias is simpler.

## Before (Deprecated)

```kotlin
class UserId(value: String)
```

## After (Modern)

```kotlin
typealias UserId = String
```

## Key Differences

- typealias is simpler
