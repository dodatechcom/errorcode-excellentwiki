---
title: "App Bundle Error"
description: "Fix Android App Bundle and Play App Signing configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Android App Bundle fails to build or upload to Play Console

## Common Causes

- App Bundle not configured in build.gradle
- Split APK configuration incorrect
- Play App Signing not properly set up
- Bundle file too large for Play Console

## Fixes

- Configure app bundle in build.gradle
- Test bundle locally with bundletool
- Set up Play App Signing in Play Console
- Reduce bundle size with resource optimization

## Code Example

```kotlin
// build.gradle
android {
    bundle {
        language {
            enableSplit = true
        }
        density {
            enableSplit = true
        }
        abi {
            enableSplit = true
        }
    }
}

// Build bundle:
./gradlew bundleRelease

// Test locally:
java -jar bundletool.jar install --bundle=app.aab
```

# App Bundle: generates optimized APKs
# bundletool: test bundles locally
# Play App Signing: managed by Google
# Reduce size: optimize resources, remove unused
