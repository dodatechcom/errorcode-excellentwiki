---
title: "[Solution] Hilt Dependency Injection Error Fix"
description: "Fix Hilt DI errors when dependency injection fails in Android or Kotlin projects."
languages: ["kotlin"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hilt", "dependency-injection", "Dagger", "Android", "kotlin"]
weight: 5
---

# Hilt: Dependency Injection Error Fix

A Hilt dependency injection error occurs when Hilt cannot provide a required dependency, module configuration is wrong, or component hierarchy is misconfigured.

## What This Error Means

Hilt manages dependency injection using Dagger under the hood. Errors occur when dependencies can't be provided, scopes are wrong, or module bindings are missing.

## Common Causes

- Missing `@Inject` on constructor
- No `@Module` providing the dependency
- Wrong scope annotation (`@Singleton` vs `@ActivityScoped`)
- Circular dependency between classes
- Missing `@AndroidEntryPoint` on Activity/Fragment

## How to Fix

### 1. Provide dependencies correctly

```kotlin
// WRONG: Missing @Inject
class UserRepository {
    fun getData() = emptyList()
}

// CORRECT: Add @Inject constructor
class UserRepository @Inject constructor(
    private val api: ApiService
) {
    fun getData() = api.fetchUsers()
}
```

### 2. Create modules for external dependencies

```kotlin
// CORRECT: Provide via module
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun provideApiService(): ApiService {
        return Retrofit.Builder()
            .baseUrl("https://api.example.com/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService::class.java)
    }
}
```

### 3. Use correct scopes

```kotlin
// CORRECT: Match scope to lifecycle
@Singleton  // App-wide
class UserRepository @Inject constructor()

@ActivityScoped  // Per activity
class SearchManager @Inject constructor()

@ViewModelScoped  // Per view model
class SearchViewModel @Inject constructor(
    private val searchManager: SearchManager
)
```

### 4. Add Android entry points

```kotlin
// CORRECT: Annotate Android components
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    @Inject lateinit var repository: UserRepository
}
```

## Related Errors

- [Koin Error](koin-error-v2) — alternative DI framework
- [Room Error](room-error-v2) — database errors
- [Kotlinx Coroutines Error](kotlinx-coroutines-error-v2) — coroutine issues
