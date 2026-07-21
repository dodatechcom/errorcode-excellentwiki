---
title: "Kotlin Serialization R8 Error"
description: "Fix R8 errors with Kotlin serialization annotations in Android release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Kotlin serialization fails in release build because R8 removes serializer classes

## Common Causes

- @Serializable class serializer removed by R8
- Kotlinx.serialization plugin generates code R8 strips
- Serializer companion object obfuscated
- Polymorphic serializer hierarchy broken

## Fixes

- Keep kotlinx.serialization rules in proguard-rules.pro
- Use @Keep on serializable data classes
- Add keep rule for generated Companion
- Use explicit serializer references in code

## Code Example

```kotlin
# kotlinx.serialization rules
-keepattributes *Annotation*, InnerClasses
-dontnote kotlinx.serialization.AnnotationsKt

-keepclassmembers class kotlinx.serialization.json.** {
    *** Companion;
}
-keepclasseswithmembers class kotlinx.serialization.json.** {
    kotlinx.serialization.KSerializer serializer(...);
}

-keep,includedescriptorclasses class com.example.**$$serializer { *; }
-keepclassmembers class com.example.** {
    *** Companion;
}
-keepclasseswithmembers class com.example.** {
    kotlinx.serialization.KSerializer serializer(...);
}
```

# Ensure plugin is applied
plugins {
    id 'org.jetbrains.kotlin.plugin.serialization' version '1.9.0'
}
