---
title: "Missing ProGuard Keep Rule"
description: "Add missing ProGuard and R8 keep rules for common Android libraries"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Library functionality breaks in release because its proguard rules are incomplete

## Common Causes

- Library AAR missing consumer proguard rules
- Custom code uses reflection without keep rules
- Kotlin serializable class not kept
- Data binding generated code stripped by R8

## Fixes

- Add keep rules to proguard-rules.pro
- Use consumerProguardFiles in library module
- Mark reflection-using classes with @Keep
- Add dontwarn for missing optional classes

## Code Example

```kotlin
# In library module's build.gradle:
android {
    defaultConfig {
        consumerProguardFiles "consumer-rules.pro"
    }
}

# consumer-rules.pro
-keep class com.library.models.** { *; }
-dontwarn com.library.optional.**
```

# Create consumer-rules.pro in library module
# R8 will merge rules from all AAR dependencies
