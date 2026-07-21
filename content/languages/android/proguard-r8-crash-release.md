---
title: "R8 Release Crash"
description: "Fix release-only crashes caused by R8 code shrinking and obfuscation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App works in debug but crashes in release because R8 removed critical code

## Common Causes

- R8 stripped a class needed at runtime via reflection
- Enum values removed that are accessed by name
- Gson model fields obfuscated causing JSON parse failure
- WebView JavaScript interface class removed

## Fixes

- Add keep rules for all reflection-using classes
- Keep enum values with -keepclassmembers
- Use @SerializedName on Gson fields or keep JSON models
- Keep JavaScript interface classes explicitly

## Code Example

```kotlin
# Gson model keep rules
-keepclassmembers class com.example.models.** {
    <fields>;
}
-keep class com.example.models.** { *; }

# Enum keep
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}
```

# Test release build early
./gradlew assembleRelease
# Install and test: adb install -r app/build/outputs/apk/release/app-release.apk
