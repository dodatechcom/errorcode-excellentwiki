---
title: "ProGuard Mapping Error"
description: "Fix ProGuard R8 mapping file and deobfuscation errors in release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Crash reports in release builds are obfuscated and hard to read

## Common Causes

- Mapping file not uploaded to crash reporting
- R8 obfuscation too aggressive breaking stack traces
- Build type not configured to output mapping
- Crashlytics not configured for deobfuscation

## Fixes

- Upload mapping.txt to Firebase Crashlytics
- Configure R8 to keep line numbers
- Verify release buildType generates mapping
- Use retrace tool for manual deobfuscation

## Code Example

```kotlin
android {
    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'),
                'proguard-rules.pro'
        }
    }
}

// Firebase auto-uploads mapping with google-services plugin
// Manual upload:
// ./gradlew assembleRelease
// Upload app/build/outputs/mapping/release/mapping.txt
```

# Retrace obfuscated stack traces:
# retrace mapping.txt obfuscated_stacktrace.txt
# Or in Android Studio: Tools > Android > Deobfuscate
