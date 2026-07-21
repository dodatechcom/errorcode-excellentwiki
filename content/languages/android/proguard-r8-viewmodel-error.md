---
title: "ViewModel R8 Error"
description: "Fix R8 errors with ViewModel and SavedStateHandle in release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewModel factory or SavedStateHandle fails in release due to R8 stripping

## Common Causes

- ViewModel factory method removed by R8
- SavedStateHandle constructor obfuscated
- AssistedInject factory stripped
- ViewModel key generation changed by obfuscation

## Fixes

- Keep ViewModel factories explicitly
- Keep SavedStateHandle constructor
- Use @Keep on ViewModel classes
- Keep AssistedInject factory interfaces

## Code Example

```kotlin
# ViewModel keep rules
-keep class * extends androidx.lifecycle.ViewModel
-keep class * extends androidx.lifecycle.AndroidViewModel
-keepclassmembers class * {
    <init>(...);
}

# SavedStateHandle
-keep class * extends androidx.lifecycle.SavedStateHandle
-keep class * extends androidxSavedStateViewModelFactory { *; }
```

# Use Hilt or Koin for ViewModel injection
# These frameworks provide their own ProGuard rules
