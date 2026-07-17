---
title: "[Solution] Kotlin Ktor Serialization Error Fix"
description: "Fix Ktor serialization errors. Learn why Ktor content negotiation fails and how to handle serialization issues."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Ktor serialization error occurs when content negotiation fails during request or response serialization. This can happen due to missing serialization plugin or wrong content type.

## Common Causes

- ContentNegotiation plugin not installed
- Missing @Serializable annotation
- Wrong content type header
- Serializer not registered

## How to Fix

```kotlin
// WRONG: Not installing ContentNegotiation
val client = HttpClient()
val response = client.post("https://api.example.com") {
    setBody(User("Alice"))  // May fail
}

// CORRECT: Install ContentNegotiation
val client = HttpClient {
    install(ContentNegotiation) {
        json()
    }
}
```

```kotlin
// WRONG: Wrong content type
val response = client.post("https://api.example.com") {
    contentType(ContentType.Text.Plain)
    setBody(User("Alice"))  // Wrong content type
}

// CORRECT: Match content type to serializer
val response = client.post("https://api.example.com") {
    contentType(ContentType.Application.Json)
    setBody(User("Alice"))
}
```

## Examples

```kotlin
// Example 1: Client serialization
val client = HttpClient {
    install(ContentNegotiation) {
        json(Json { ignoreUnknownKeys = true })
    }
}

val user: User = client.get("https://api.example.com/user").body()

// Example 2: Server serialization
fun Application.module() {
    install(ContentNegotiation) {
        json()
    }
    routing {
        get("/user") {
            call.respond(User("Alice", 30))
        }
    }
}

// Example 3: Custom serializer
install(ContentNegotiation) {
    json(Json {
        prettyPrint = true
        isLenient = true
        ignoreUnknownKeys = true
    })
}
```

## Related Errors

- [Ktor request error](ktor-requesterror) — request failed
- [Ktor routing error](ktor-routingerror) — routing failed
- [SerializationException](serializationexception) — kotlinx.serialization failed
