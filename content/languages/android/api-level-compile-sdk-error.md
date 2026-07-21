---
title: "Compile SDK Version Error"
description: "Fix compileSdkVersion errors and targetSdkVersion mismatch in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because compileSdkVersion is too low for used APIs or dependencies

## Common Causes

- compileSdk lower than library required SDK
- targetSdkVersion not matching compileSdkVersion
- Missing SDK platform in SDK Manager
- Using API from SDK not yet installed

## Fixes

- Set compileSdk to latest stable (34 for 2024)
- Match targetSdkVersion to compileSdkVersion
- Install required SDK platform via SDK Manager
- Update build.gradle to use latest SDK

## Code Example

```kotlin
android {
    compileSdk = 34
    defaultConfig {
        targetSdk = 34
        minSdk = 24
    }
}
```

# Check installed SDKs
$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --list_installed
# Install missing platform
sdkmanager "platforms;android-34" 
