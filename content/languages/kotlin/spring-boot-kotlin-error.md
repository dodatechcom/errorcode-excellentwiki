---
title: "[Solution] Spring Boot Kotlin Null Safety Error Fix"
description: "Fix Spring Boot Kotlin null safety errors when Java interop causes unexpected nulls."
languages: ["kotlin"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring-boot", "kotlin", "null-safety", "nullable", "jvm"]
weight: 5
---

# Spring Boot: Kotlin Null Safety Error Fix

A Spring Boot Kotlin null safety error occurs when Kotlin's null safety is bypassed by Java interop, framework annotations, or uninitialized properties.

## What This Error Means

Kotlin enforces null safety at compile time, but Spring Boot (written in Java) can return null from annotated methods. This causes `NullPointerException` at runtime when Kotlin code expects non-null values.

## Common Causes

- Java methods returning null where Kotlin expects non-null
- Spring Data repositories returning null
- `@Autowired` properties not injected
- Request parameters not validated
- Jackson deserialization producing nulls

## How to Fix

### 1. Use nullable types for Spring interop

```kotlin
// WRONG: Java interop may return null
@Service
class UserService {
    @Autowired
    lateinit var repository: UserRepository  // NPE if not injected

    fun findById(id: Long): User = repository.findById(id).get()  // May be null!
}

// CORRECT: Use nullable types
@Service
class UserService(
    private val repository: UserRepository
) {
    fun findById(id: Long): User? = repository.findById(id).orElse(null)
}
```

### 2. Use Kotlin-first Spring features

```kotlin
// CORRECT: Constructor injection (recommended)
@Service
class UserService(private val repository: UserRepository) {
    fun findAll(): List<User> = repository.findAll()
}

// CORRECT: Use Spring's null-safe annotations
fun findUser(@RequestParam id: Long): ResponseEntity<User> {
    return repository.findById(id)
        .map { ResponseEntity.ok(it) }
        .orElse(ResponseEntity.notFound().build())
}
```

### 3. Validate request bodies

```kotlin
// CORRECT: Use validation annotations
data class CreateUserRequest(
    @field:NotBlank val name: String,
    @field:Email val email: String
)

@PostMapping("/users")
fun createUser(@Valid @RequestBody request: CreateUserRequest): User {
    return userService.create(request)
}
```

### 4. Handle optional results

```kotlin
// CORRECT: Use Kotlin's null safety with Spring
@GetMapping("/users/{id}")
fun getUser(@PathVariable id: Long): ResponseEntity<User> {
    return userService.findById(id)
        ?.let { ResponseEntity.ok(it) }
        ?: ResponseEntity.notFound().build()
}
```

## Related Errors

- [Ktor Request Error](ktor-request-error-v2) — Ktor pipeline issues
- [Exposed Error](exposed-error-v2) — database errors
- [Kotlinx Coroutines Error](kotlinx-coroutines-error-v2) — coroutine issues
