---
title: "[Solution] Ktor Routing Conflict Error Fix"
description: "Fix Ktor routing errors when route definitions conflict or overlap."
languages: ["kotlin"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Ktor: Routing Conflict Error Fix

A Ktor routing error occurs when multiple route definitions conflict, overlap, or have ambiguous patterns.

## What This Error Means

Ktor uses a routing tree to match incoming requests. Conflicts occur when two routes match the same path, or when route parameters overlap with static segments.

## Common Causes

- Duplicate route paths with different methods
- Route parameter conflicts with static paths
- Nested routes with overlapping patterns
- Missing route for a specific HTTP method

## How to Fix

### 1. Avoid duplicate routes

```kotlin
// WRONG: Duplicate routes
routing {
    get("/users") { call.respond("list") }
    get("/users") { call.respond("duplicate") }  // Conflict!
}

// CORRECT: Use different paths or methods
routing {
    get("/users") { call.respond("list") }
    post("/users") { call.respond("create") }
}
```

### 2. Order routes correctly

```kotlin
// CORRECT: Static routes before parameterized
routing {
    get("/users/me") { call.respond("current user") }  // Static first
    get("/users/{id}") { call.respond("user by id") }   // Parameter after
}
```

### 3. Use route groups

```kotlin
// CORRECT: Organize with route groups
routing {
    route("/api/v1") {
        route("/users") {
            get { call.respond("list users") }
            post { call.respond("create user") }
            get("/{id}") { call.respond("get user") }
        }
        route("/posts") {
            get { call.respond("list posts") }
        }
    }
}
```

### 4. Handle method-specific routes

```kotlin
// CORRECT: Explicit method routing
routing {
    route("/items") {
        method(HttpMethod.Get) {
            call.respond("list items")
        }
        method(HttpMethod.Post) {
            call.respond("create item")
        }
    }
}
```

## Related Errors

- [Ktor Request Error](ktor-request-error-v2) — request pipeline issues
- [Spring Boot Kotlin Error](spring-boot-kotlin-error) — Spring Boot issues
- [Hilt Error](hilt-error-v2) — dependency injection
