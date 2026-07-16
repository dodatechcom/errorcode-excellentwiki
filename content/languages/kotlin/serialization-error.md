---
title: "[Solution] Kotlin SerializationException — Serialization Fix"
description: "Fix Kotlin SerializationException when serializing or deserializing objects. Check class annotations, serializer compatibility, and data structure."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["serializationexception", "serialization", "json", "serializable", "encode"]
weight: 5
---

# SerializationException — Serialization Fix

A `SerializationException` is thrown when Kotlin serialization fails due to incompatible types, missing annotations, or unsupported data structures. This is common with `kotlinx.serialization` and other serialization frameworks.

## Description

Kotlin's `kotlinx.serialization` requires classes to be annotated with `@Serializable` and have compatible serializers. Exceptions occur when trying to serialize non-serializable types, using wrong serializers, or encountering unexpected data structures.

Common scenarios:

- **Missing @Serializable annotation** — class not marked for serialization.
- **Non-serializable property** — class has properties that can't be serialized.
- **Wrong serializer** — using serializer for wrong type.
- **Circular references** — object graph with cycles.
- **Polymorphic serialization issues** — sealed class not configured.

## Common Causes

```kotlin
// Cause 1: Missing @Serializable
class User(val name: String, val age: Int)
val json = Json.encodeToString(user)  // SerializationException

// Cause 2: Non-serializable property
@Serializable
class Config(val handler: () -> Unit)  // Function not serializable

// Cause 3: Wrong serializer
@Serializable
data class Point(val x: Int, val y: Int)
val json = Json.encodeToString(String.serializer(), Point(1, 2))
// SerializationException: wrong serializer

// Cause 4: Circular reference
@Serializable
class Node(val value: Int, var next: Node? = null)
val a = Node(1)
val b = Node(2)
a.next = b
b.next = a  // Circular reference
Json.encodeToString(a)  // SerializationException or StackOverflow
```

## Solutions

### Fix 1: Add @Serializable annotation

```kotlin
// Wrong — missing annotation
class User(val name: String, val age: Int)

// Correct
@Serializable
class User(val name: String, val age: Int)
```

### Fix 2: Use @Transient for non-serializable properties

```kotlin
// Wrong
@Serializable
class Config(val handler: () -> Unit)  // Function not serializable

// Correct
@Serializable
class Config(
    val name: String,
    @Transient val handler: () -> Unit = {}
)
```

### Fix 3: Use correct serializer

```kotlin
// Wrong — wrong serializer
val json = Json.encodeToString(String.serializer(), Point(1, 2))

// Correct — use correct serializer
val json = Json.encodeToString(Point.serializer(), Point(1, 2))

// Or let type inference handle it
val json = Json.encodeToString(Point(1, 2))
```

### Fix 4: Handle sealed classes properly

```kotlin
// Wrong — sealed class without polymorphic config
@Serializable
sealed class Shape {
    @Serializable
    data class Circle(val radius: Double) : Shape()
    @Serializable
    data class Rect(val w: Double, val h: Double) : Shape()
}

// Correct — use polymorphic serialization
val json = Json {
    classDiscriminator = "type"
}
val shape: Shape = Shape.Circle(5.0)
val encoded = json.encodeToString(Shape.serializer(), shape)
```

## Examples

```kotlin
import kotlinx.serialization.*
import kotlinx.serialization.json.*

@Serializable
data class User(
    val name: String,
    val age: Int,
    @Transient val internalId: Long = 0
)

fun main() {
    val user = User("Alice", 30, 12345L)
    val json = Json.encodeToString(user)
    println(json)  // {"name":"Alice","age":30}

    val decoded = Json.decodeFromString<User>(json)
    println(decoded)  // User(name=Alice, age=30, internalId=0)
}
```

## Related Errors

- [JsonDecodingException]({{< relref "/languages/kotlin/json-parse-error" >}}) — JSON parsing failed.
- [JsonEncodingException]({{< relref "/languages/kotlin/json-encoding-error" >}}) — JSON encoding failed.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid serialization config.
