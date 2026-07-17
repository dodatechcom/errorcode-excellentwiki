---
title: "[Solution] Kotlin JsonDecodingException — JSON Parse Fix"
description: "Fix Kotlin JsonDecodingException when parsing JSON. Validate JSON structure, check type compatibility, and handle missing fields."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# JsonDecodingException — JSON Parse Fix

A `JsonDecodingException` is thrown when `kotlinx.serialization` cannot decode a JSON string into the target class. The JSON structure doesn't match the expected data class.

## Description

This exception occurs during `Json.decodeFromString()` when the JSON is malformed, has unexpected types, or is missing required fields. The exception message includes details about what went wrong.

Common scenarios:

- **Wrong JSON structure** — nested objects in wrong places.
- **Type mismatch** — JSON has string where Int is expected.
- **Missing required fields** — JSON missing fields without defaults.
- **Malformed JSON** — syntax errors in JSON string.
- **Unknown keys** — JSON has keys not in the data class (when configured to ignore).

## Common Causes

```kotlin
// Cause 1: Type mismatch
@Serializable
data class User(val name: String, val age: Int)
val json = """{"name": "Alice", "age": "thirty"}"""  // age is String, not Int
Json.decodeFromString<User>(json)  // JsonDecodingException

// Cause 2: Missing required field
val json = """{"name": "Alice"}"""  // Missing 'age'
Json.decodeFromString<User>(json)  // JsonDecodingException

// Cause 3: Malformed JSON
val json = """{"name": "Alice", "age": 30"""  // Missing closing brace
Json.decodeFromString<User>(json)  // JsonDecodingException

// Cause 4: Wrong structure
val json = """[{"name": "Alice"}, {"name": "Bob"}]"""  // Array, not object
Json.decodeFromString<User>(json)  // JsonDecodingException
```

## Solutions

### Fix 1: Validate JSON structure

```kotlin
// Wrong — assuming JSON is always valid
val user = Json.decodeFromString<User>(untrustedJson)

// Correct — handle parsing errors
val user = try {
    Json.decodeFromString<User>(untrustedJson)
} catch (e: JsonDecodingException) {
    println("Invalid JSON: ${e.message}")
    null
}
```

### Fix 2: Add default values for optional fields

```kotlin
// Wrong — all fields required
@Serializable
data class User(val name: String, val age: Int)

// Correct — age has default
@Serializable
data class User(val name: String, val age: Int = 0)

// JSON without age still works
val json = """{"name": "Alice"}"""
val user = Json.decodeFromString<User>(json)  // User("Alice", 0)
```

### Fix 3: Configure Json to be lenient

```kotlin
// Wrong — strict parsing
val json = Json { ignoreUnknownKeys = false }

// Correct — ignore unknown keys
val json = Json {
    ignoreUnknownKeys = true
    isLenient = true
    coerceInputValues = true  // Use defaults for null/unknown values
}
```

### Fix 4: Use nullable types for optional data

```kotlin
// Wrong — non-nullable
@Serializable
data class User(val name: String, val age: Int)

// Correct — nullable age
@Serializable
data class User(val name: String, val age: Int? = null)

val json = """{"name": "Alice"}"""
val user = Json.decodeFromString<User>(json)  // User("Alice", null)
```

## Examples

```kotlin
import kotlinx.serialization.*
import kotlinx.serialization.json.*

@Serializable
data class User(
    val name: String,
    val age: Int = 0,
    val email: String? = null
)

fun main() {
    val json = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
    }

    val validJson = """{"name": "Alice", "age": 30}"""
    val user = json.decodeFromString<User>(validJson)
    println(user)  // User(name=Alice, age=30, email=null)

    val invalidJson = """{"name": "Bob", "age": "invalid"}"""
    try {
        val user2 = json.decodeFromString<User>(invalidJson)
    } catch (e: JsonDecodingException) {
        println("Parse error: ${e.message}")
    }
}
```

## Related Errors

- [JsonEncodingException]({{< relref "/languages/kotlin/json-encoding-error" >}}) — JSON encoding failed.
- [SerializationException]({{< relref "/languages/kotlin/serialization-error" >}}) — general serialization error.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid input data.
