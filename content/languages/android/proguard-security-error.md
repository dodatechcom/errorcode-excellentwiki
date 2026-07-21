---
title: "ProGuard Security Error"
description: "Fix ProGuard security rules to prevent reverse engineering of Android apps"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App is easily reverse-engineered because security rules are not configured

## Common Causes

- R8/ProGuard obfuscation not enabled in release
- Native code not stripped of debug symbols
- API keys hardcoded in source
- Build config exposes sensitive information

## Fixes

- Enable minifyEnabled and shrinkResources
- Strip debug symbols from native libraries
- Store API keys in BuildConfig or environment variables
- Use BuildConfig fields for sensitive values

## Code Example

```kotlin
android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'),
                'proguard-rules.pro'
        }
    }
}

// Store API key securely:
buildConfigField("String", "API_KEY", ""${System.getenv('API_KEY')}"")

// Native code stripping:
android {
    packagingOptions {
        doNotStrip '*/arm64-v8a/*.so'  // Keep for debugging
    }
}
```

# Always enable R8 for release builds
# Never commit API keys to source control
# Use BuildConfig or local.properties
