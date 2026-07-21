---
title: "Retrofit R8 Converter Error"
description: "Fix Retrofit converter factory errors when R8 strips serialization code"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit converters fail to serialize/deserialize in release builds

## Common Causes

- Converter factory class stripped by R8
- Gson type adapter removed by R8
- Moshi codegen adapter not kept
- Serialization annotations stripped

## Fixes

- Keep converter factories in proguard rules
- Keep model classes and their serializers
- Use @Keep annotation on critical classes
- Add keep rules for specific serialization libraries

## Code Example

```kotlin
# proguard-rules.pro
# Gson
-keepattributes Signature
-keepattributes *Annotation*
-keep class com.google.gson.** { *; }
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}

# Moshi
-keep class com.squareup.moshi.** { *; }
-keepclassmembers class * {
    @com.squareup.moshi.Json <fields>;
}

# Retrofit converters
-keep class retrofit2.converter.gson.** { *; }
-keep class retrofit2.converter.moshi.** { *; }
```

# Keep serialization annotations
# Keep model classes with their fields
# Keep converter factory classes
