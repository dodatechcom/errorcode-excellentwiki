---
title: "Kotlin Serialization Error"
description: "Fix Kotlin serialization and deserialization errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Kotlin serialization plugin fails to generate serializer or JSON parsing fails

## Common Causes

- @Serializable annotation missing on data class
- kotlinx.serialization plugin not applied
- JSON field names do not match property names
- Missing default values for optional fields

## Fixes

- Add @Serializable annotation to data class
- Apply kotlin serialization Gradle plugin
- Use @SerialName for JSON key mapping
- Provide default values for optional properties

## Code Example

```kotlin
@Serializable
data class User(
    val id: Long,
    val name: String,
    @SerialName("email_address") val email: String,
    val age: Int = 0  // Default value
)

// Serialize:
val json = Json.encodeToString(user)

// Deserialize:
val user = Json.decodeFromString<User>(jsonString)

// Configure JSON:
val json = Json {
    ignoreUnknownKeys = true
    coerceInputValues = true
    prettyPrint = true
}
```

# Plugin: id 'org.jetbrains.kotlin.plugin.serialization'
# @Serializable on each data class
# @SerialName for custom JSON keys
