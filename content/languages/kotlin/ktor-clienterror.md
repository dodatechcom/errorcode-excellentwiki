---
title: "[Solution] Kotlin Ktor Client Engine Error Fix"
description: "Fix Ktor client engine errors. Learn why Ktor client engine fails and how to configure the HTTP client engine."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["ktor", "client", "engine", "http", "kotlin"]
weight: 5
---

## What This Error Means

A Ktor client engine error occurs when the HTTP client engine fails to initialize or execute. Ktor supports multiple engines (CIO, OkHttp, Apache, Java), and configuration issues can cause failures.

## Common Causes

- Missing engine dependency
- Engine not compatible with platform
- Wrong engine configuration
- Thread pool exhaustion

## How to Fix

```kotlin
// WRONG: Missing engine dependency
val client = HttpClient()  // May fail without engine

// CORRECT: Specify engine explicitly
val client = HttpClient(CIO) {
    // Configure engine
}
```

```kotlin
// WRONG: Wrong engine for platform
// Android cannot use Java engine
val client = HttpClient(Java) {
    // Fails on Android
}

// CORRECT: Use platform-appropriate engine
// Android
val client = HttpClient(OkHttp) { }

// JVM
val client = HttpClient(CIO) { }
```

## Examples

```kotlin
// Example 1: CIO engine
val client = HttpClient(CIO) {
    install(ContentNegotiation) { json() }
    expectSuccess = false
}

// Example 2: OkHttp engine
val client = HttpClient(OkHttp) {
    install(ContentNegotiation) { json() }
    engine {
        config {
            retryOnConnectionFailure(true)
        }
    }
}

// Example 3: Engine configuration
val client = HttpClient(CIO) {
    engine {
        threadsCount = 4
        pipelining = true
        maxConnectionsPerRoute = 100
    }
}
```

## Related Errors

- [Ktor request error](ktor-requesterror) — request failed
- [Ktor serialization error](ktor-serializationerror) — serialization failed
- [OkHttp connection error](okhttp-error-kotlin) — OkHttp issue
