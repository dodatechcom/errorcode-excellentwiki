---
title: "Backward Compatibility Error"
description: "Fix backward compatibility issues when supporting multiple Android API levels"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App works on newer devices but crashes or misbehaves on older Android versions

## Common Causes

- Using Material3 component on API < 21
- Java 8 feature used without desugaring
- Kotlin coroutines on very old API levels
- ViewBinding not working on legacy devices

## Fixes

- Enable coreLibraryDesugaring for Java 8+ APIs
- Use AppCompat or AndroidX for backward compatibility
- Provide alternate layouts for different API levels
- Use version checks for all newer API calls

## Code Example

```kotlin
android {
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    defaultConfig {
        coreLibraryDesugaringEnabled true
    }
}

dependencies {
    coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:2.0.4'
}
```

# Use res/layout-v21/ for API 21+ layouts
# Use res/values-v21/ for API 21+ values
# Android automatically picks correct qualifier
