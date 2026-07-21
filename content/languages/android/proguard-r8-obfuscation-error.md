---
title: "R8 Obfuscation Error"
description: "Fix R8 obfuscation errors that break serialization and reflection in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Classes or fields are renamed by R8 causing runtime reflection failures

## Common Causes

- Data class fields renamed breaking JSON parsing
- Retrofit interface methods obfuscated
- Room entity fields renamed
- Parcelable Creator field names changed

## Fixes

- Add @Keep annotation to serializable classes
- Use @SerializedName for Gson fields
- Keep Retrofit interfaces explicitly
- Add -keepnames for Parcelable CREATOR

## Code Example

```kotlin
# Keep Retrofit interfaces
-keep,allowobfuscation interface * {
    @retrofit2.http.* <methods>;
}

# Keep JSON models
-keep class com.example.api.models.** { *; }

# Prevent obfuscation of specific packages
-renamesourcefileattribute SourceFile
-keepattributes SourceFile,LineNumberTable
```

# Full R8 rules for common libraries:
# Retrofit, Gson, Moshi, Room each have
# recommended rules in their documentation
