---
title: "Min SDK Version Error"
description: "Fix Android minSdkVersion errors during manifest merge or install"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App or library requires a minimum API level higher than configured

## Common Causes

- Library declares higher minSdk than app
- Using API not available at configured minSdk
- Manifest merger conflict on minSdk attribute
- Device running Android version below minSdk

## Fixes

- Increase minSdkVersion to match library requirement
- Use @RequiresApi annotation for newer API calls
- Check manifest merger report for conflicts
- Use Build.VERSION.SDK_INT checks at runtime

## Code Example

```kotlin
android {
    defaultConfig {
        minSdk = 24  // Must be >= highest library minSdk
    }
}
```

# Find which library requires higher SDK
./gradlew :app:processDebugManifest --info
# Check merger report for minSdk conflicts
