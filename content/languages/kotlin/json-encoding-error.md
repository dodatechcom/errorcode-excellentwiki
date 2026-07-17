---
title: "[Solution] Kotlin JsonEncodingException — JSON Encode Fix"
description: "Fix Kotlin JsonEncodingException when encoding objects to JSON. Check serializable types, handle nullable fields, and configure Json properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# JsonEncodingException — JSON Encode Fix

A `JsonEncodingException` is thrown when `kotlinx.serialization` cannot encode an object to JSON. This occurs with unsupported types, circular references, or encoding configuration issues.

## Description

This exception occurs during `Json.encodeToString()` when the object cannot be converted to JSON. Unlike `JsonDecodingException` (input parsing), this happens during output generation.

Common scenarios:

- **Non-serializable type** — trying to encode a type without serializer.
- **Circular references** — object graph with cycles.
- **Unsupported content** — special characters in strings.
- **Class not marked @Serializable** — missing annotation.
- **Polymorphic encoding issues** — sealed class not configured.

## Common Causes

```kotlin
// Cause 1: Non-serializable type
class Handler(val callback: () -> Unit)
val json = Json.encodeToString(handler)  // JsonEncodingException

// Cause 2: Circular reference
@Serializable
class Node(val value: Int, var next: Node? = null)
val a = Node(1)
val b = Node(2)
a.next = b
b.next = a  // Circular
Json.encodeToString(a)  // JsonEncodingException or StackOverflow

// Cause 3: Missing @Serializable
class Simple(val data: String)
val json = Json.encodeToString(Simple.serializer(), Simple("test"))
// SerializationException (JsonEncodingException subtype)

// Cause 4: Encoding null to non-nullable
@Serializable
data class Config(val name: String)
val config = Config(null as String?)  // May throw
```

## Solutions

### Fix 1: Mark classes as @Serializable

```kotlin
// Wrong
class User(val name: String)

// Correct
@Serializable
class User(val name: String)
```

### Fix 2: Handle circular references

```kotlin
// Wrong — circular reference
@Serializable
class Node(val value: Int, var next: Node? = null)
val a = Node(1)
val b = Node(2)
a.next = b
b.next = a

// Correct — break circular reference before encoding
@Serializable
class Node(val value: Int, var next: Node? = null) {
    fun toAcyclic(visited: MutableSet<Node> = mutableSetOf()): Node {
        if (!visited.add(this)) return Node(value, null)
        return Node(value, next?.toAcyclic(visited))
    }
}
val encoded = Json.encodeToString(a.toAcyclic())
```

### Fix 3: Use @Transient for non-serializable properties

```kotlin
// Wrong
@Serializable
class Config(val handler: () -> Unit)

// Correct
@Serializable
class Config(
    val name: String,
    @Transient val handler: () -> Unit = {}
)
```

### Fix 4: Configure Json for encoding

```kotlin
// Wrong — default strict mode
val json = Json { }

// Correct — configure for your needs
val json = Json {
    prettyPrint = true
    encodeDefaults = true  // Encode properties with default values
    ignoreUnknownKeys = true
}
```

## Examples

```kotlin
import kotlinx.serialization.*
import kotlinx.serialization.json.*

@Serializable
data class User(
    val name: String,
    val age: Int,
    @Transient val temporaryToken: String? = null
)

fun main() {
    val user = User("Alice", 30, "token123")

    // temporaryToken excluded due to @Transient
    val json = Json.encodeToString(user)
    println(json)  // {"name":"Alice","age":30}

    // Pretty printed
    val prettyJson = Json { prettyPrint = true }.encodeToString(user)
    println(prettyJson)
}
```

## Related Errors

- [JsonDecodingException]({{< relref "/languages/kotlin/json-parse-error" >}}) — JSON parsing failed.
- [SerializationException]({{< relref "/languages/kotlin/serialization-error" >}}) — general serialization error.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid encoding config.
