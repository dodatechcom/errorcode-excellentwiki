---
title: "[Solution] Kotlin Hilt Dependency Injection Error Fix"
description: "Fix Hilt dependency injection errors in Kotlin. Learn why Hilt injection fails and how to configure DI properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["hilt", "dependency-injection", "di", "kotlin"]
weight: 5
---

## What This Error Means

A Hilt dependency injection error occurs when Hilt cannot provide or inject dependencies. This can happen due to missing annotations, circular dependencies, or configuration issues.

## Common Causes

- Missing @Inject annotation
- Missing @Module or @Provides
- Circular dependency
- Wrong component scope

## How to Fix

```kotlin
// WRONG: Missing @Inject
class UserService {
    fun findAll(): List<User> = // ...
}
// Cannot inject UserService

// CORRECT: Add @Inject
class UserService @Inject constructor(
    private val repository: UserRepository
) {
    fun findAll(): List<User> = repository.findAll()
}
```

```kotlin
// WRONG: Missing module for interface
interface UserRepository {
    fun findAll(): List<User>
}
// Hilt doesn't know how to provide UserRepository

// CORRECT: Provide with module
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository
}
```

## Examples

```kotlin
// Example 1: Basic Hilt setup
@HiltAndroidApp
class MyApplication : Application()

// Example 2: Activity injection
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    @Inject lateinit var userService: UserService
}

// Example 3: ViewModel injection
@HiltViewModel
class UserViewModel @Inject constructor(
    private val repository: UserRepository
) : ViewModel() {
    val users = repository.findAll()
}
```

## Related Errors

- [Koin dependency injection error](koin-error) — Koin DI error
- [Spring Boot Kotlin error](spring-boot-kotlin) — Spring Boot error
- [Room database error](room-error) — Room error
