---
title: "Moshi Adapter Error"
description: "Fix Moshi JSON adapter and reflection errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Moshi fails to create adapter for custom type or uses wrong adapter

## Common Causes

- Moshi not configured with KotlinJsonAdapterFactory
- Class has non-default constructor without @Json
- Adapter generated at compile time not available
- Polymorphic type not configured

## Fixes

- Add KotlinJsonAdapterFactory to Moshi builder
- Use @JsonClass(generateAdapter = true) for codegen
- Use @Json for non-data classes
- Configure polymorphic adapter for sealed classes

## Code Example

```kotlin
// Moshi with Kotlin support
val moshi = Moshi.Builder()
    .addLast(KotlinJsonAdapterFactory())
    .build()

val adapter = moshi.adapter(User::class.java)

// For codegen (recommended):
@JsonClass(generateAdapter = true)
data class User(
    val name: String,
    val email: String
)

// With custom adapter:
val adapter = moshi.adapter(User::class.java).lenient()
```

# Moshi dependencies:
# implementation 'com.squareup.moshi:moshi:1.15.0'
# kapt 'com.squareup.moshi:moshi-kotlin-codegen:1.15.0'
# Use codegen for better performance
