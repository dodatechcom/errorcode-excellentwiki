---
title: "[Solution] Deprecated Function Migration: lateinit to nullable or lazy init"
description: "Migrate from deprecated lateinit to nullable or lazy initialization."
deprecated_function: "lateinit var x: Type"
replacement_function: "var x: Type? = null or lazy {}"
languages: ["kotlin"]
deprecated_since: "Kotlin 1.0+"
---

# [Solution] Deprecated Function Migration: lateinit to nullable or lazy init

The `lateinit var x: Type` has been deprecated in favor of `var x: Type? = null or lazy {}`.

## Migration Guide

Nullable or lazy is safer than lateinit

lateinit can throw UninitializedPropertyAccessException. Nullable or lazy is safer.

## Before (Deprecated)

```kotlin
class MyService {
    lateinit var database: Database

    fun init() {
        database = Database.connect()
    }

    fun query(sql: String) {
        // might throw if not initialized
        database.execute(sql)
    }
}
```

## After (Modern)

```kotlin
class MyService {
    private var database: Database? = null

    fun init() {
        database = Database.connect()
    }

    fun query(sql: String) {
        database?.execute(sql)
    }
}

// Or with lazy
private val database by lazy { Database.connect() }
```

## Key Differences

- Nullable is always safe
- lazy initializes on first access
- lateinit for guaranteed initialization
- ::isInitialized to check lateinit
