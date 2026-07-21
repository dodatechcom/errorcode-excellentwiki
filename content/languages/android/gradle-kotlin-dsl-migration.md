---
title: "Kotlin DSL Migration Error"
description: "Fix migration from Groovy to Kotlin DSL in Android Gradle build files"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails when converting build.gradle from Groovy to Kotlin DSL

## Common Causes

- Groovy syntax not valid in Kotlin DSL
- Extension properties not accessible
- Plugin application syntax different
- String interpolation not working

## Fixes

- Replace single quotes with double quotes
- Use = for assignment instead of method call
- Apply plugins with id() function
- Use string interpolation with $variable

## Code Example

```kotlin
// Groovy:
android {
    compileSdkVersion 34
    defaultConfig {
        applicationId "com.example.app"
        minSdkVersion 24
    }
}

// Kotlin DSL:
android {
    compileSdk = 34
    defaultConfig {
        applicationId = "com.example.app"
        minSdk = 24
    }
}

// Plugin application:
plugins {
    id("com.android.application") version "8.2.0" apply false
}
```

# Groovy -> Kotlin DSL key changes:
# Single quotes -> double quotes
# method() -> method =
# apply plugin -> id()
# Check build.gradle.kts for syntax
