---
title: "[Solution] Koin Module Not Loaded Error Fix"
description: "Fix Koin dependency injection errors when modules fail to load."
languages: ["kotlin"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["koin", "module", "dependency-injection", "kotlin"]
weight: 5
---

# Koin: Module Not Loaded Error Fix

A Koin module not loaded error occurs when a Koin module fails to start or a dependency cannot be resolved.

## What This Error Means

Koin is a lightweight DI framework for Kotlin. Module errors occur when modules aren't declared, dependencies can't be resolved, or the module isn't started before use.

## Common Causes

- Module not declared in `startKoin`
- Dependency not provided in any module
- Circular dependency between definitions
- Wrong scope (using `single` vs `factory`)
- Module loaded too late

## How to Fix

### 1. Declare all modules in startKoin

```kotlin
// CORRECT: Include all modules
startKoin {
    androidContext(this@MyApplication)
    modules(appModule, networkModule, databaseModule)
}
```

### 2. Define modules correctly

```kotlin
// CORRECT: Module definition
val appModule = module {
    single { DatabaseHelper(get()) }
    factory { UserRepository(get()) }
    viewModel { MainViewModel(get(), get()) }
}
```

### 3. Resolve dependencies in correct order

```kotlin
// WRONG: Dependency order matters
val module = module {
    single { UserRepository(get()) }  // ApiService not yet defined
    single { ApiService() }
}

// CORRECT: Dependencies defined before consumers
val module = module {
    single { ApiService() }
    single { UserRepository(get()) }
}
```

### 4. Use scopes properly

```kotlin
// CORRECT: Scope for lifecycle-bound dependencies
val module = module {
    scope<MainActivity> {
        scoped { SearchManager() }
    }
    viewModel { MainViewModel(get()) }
}
```

## Related Errors

- [Hilt Error](hilt-error-v2) — alternative DI framework
- [Exposed Error](exposed-error-v2) — database errors
- [Room Error](room-error-v2) — Room database errors
