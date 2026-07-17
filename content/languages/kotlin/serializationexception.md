---
title: "[Solution] Kotlin SerializationException Fix"
description: "Fix Kotlin SerializationException in kotlinx.serialization. Learn why serialization fails and how to handle format errors."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A SerializationException is thrown when kotlinx.serialization cannot serialize or deserialize data. This happens due to missing annotations, wrong format, or missing class discriminator.

## Common Causes

- Missing @Serializable annotation
- Missing keys in JSON
- Wrong data types
- Polymorphic serialization not configured

## How to Fix

```kotlin
// WRONG: Missing @Serializable
class User(val name: String, val age: Int)
val json = Json.encodeToString(user)  // SerializationException

// CORRECT: Add @Serializable
@Serializable
class User(val name: String, val age: Int)
val json = Json.encodeToString(user)
```

```kotlin
// WRONG: Strict decoding of missing keys
@Serializable
data class User(val name: String, val email: String)
val user = Json.decodeFromString<User>("""{"name": "Alice"}""")  // Missing email

// CORRECT: Use ignoreUnknownKeys
val json = Json { ignoreUnknownKeys = true }
val user = json.decodeFromString<User>("""{"name": "Alice"}""")
```

```kotlin
// WRONG: Polymorphic serialization not configured
open class Shape
@Serializable
class Circle(val radius: Double) : Shape()

// CORRECT: Configure polymorphic serialization
val json = Json {
    polymorphic(Shape::class) {
        subclass(Circle::class)
    }
}
```

## Examples

```kotlin
// Example 1: Basic serialization
@Serializable
data class User(val name: String, val age: Int)

val user = User("Alice", 30)
val json = Json.encodeToString(user)
val decoded = Json.decodeFromString<User>(json)

// Example 2: Custom serializer
@Serializable(with = DateSerializer::class)
val date: Date

// Example 3: Ignore unknown keys
val json = Json { ignoreUnknownKeys = true }
```

## Related Errors

- [Ktor serialization error](ktor-serializationerror) — Ktor serialization failed
- [Kotlinx serialization format error](kotlinx-serialization-error) — format mismatch
- [JSON decoding error] — JSON parse failed
