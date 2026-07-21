---
title: "Retrofit Interface R8 Error"
description: "Fix R8 obfuscation of Retrofit API interfaces in Android release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit API calls fail in release because interface methods are obfuscated

## Common Causes

- Retrofit interface methods renamed by R8
- @GET/@POST annotations stripped
- Converter cannot match obfuscated method names
- Generic type information erased by R8

## Fixes

- Keep Retrofit interfaces with all annotations
- Use @Keep on API service interfaces
- Add -keepattributes for annotations
- Keep generic signature attributes

## Code Example

```kotlin
# Retrofit keep rules
-keepattributes Signature
-keepattributes *Annotation*
-keep class retrofit2.** { *; }
-keepclasseswithmembers class * {
    @retrofit2.http.* <methods>;
}

# Keep API service interfaces
-keep,allowobfuscation,allowshrinking interface com.example.api.**
-keep,allowobfuscation,allowshrinking class com.example.api.models.** { *; }
```

# Ensure retrofit2-r8 or retrofit2 proguard rules
# are included from the retrofit AAR
