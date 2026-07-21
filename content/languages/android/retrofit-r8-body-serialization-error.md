---
title: "Retrofit Body Serialization Error"
description: "Fix Retrofit body serialization errors with R8 obfuscation in release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit request body serialization fails in release builds because of R8

## Common Causes

- @Body parameter class obfuscated by R8
- Content-Type header not set correctly
- Converter factory cannot serialize obfuscated class
- Kotlin data class fields renamed in release

## Fixes

- Keep model classes in proguard rules
- Use @SerializedName or @Json annotations
- Ensure Content-Type matches converter
- Keep Retrofit converter annotations

## Code Example

```kotlin
# proguard-rules.pro
-keep class com.example.api.models.** { *; }
-keepclassmembers class com.example.api.models.** {
    <fields>;
}

// Or annotate each class:
@Keep
data class CreateUserRequest(
    val name: String,
    @SerializedName("email_address") val email: String
)
```

# @Keep prevents R8 obfuscation
# @SerializedName provides stable JSON keys
# Always keep API model classes
