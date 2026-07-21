---
title: "Incompatible Dependency API Level"
description: "Fix incompatible dependency errors caused by API level requirements"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build or runtime fails because a dependency requires higher API level

## Common Causes

- Library minSdk higher than app minSdk
- Transitive dependency brings higher API requirement
- Manifest merger fails on conflicting minSdk
- Library uses APIs not available at app's minSdk

## Fixes

- Check library minSdk in its documentation
- Increase app minSdk to match library
- Use newer library version with lower minSdk
- Isolate high-API library in feature module

## Code Example

```kotlin
// Check dependency's minSdk
./gradlew :app:dependencies

// If library requires API 21 but app is API 19:
android {
    defaultConfig {
        minSdk = 21  // Increase to match
    }
}
```

# Find which library requires higher SDK
./gradlew :app:processDebugManifest --info | grep minSdk
# Check merger report in app/build/outputs
