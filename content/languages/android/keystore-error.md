---
title: "Keystore Error"
description: "Fix Android keystore and signing configuration errors for release builds"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Release build fails because of keystore or signing configuration issues

## Common Causes

- Keystore file path incorrect in build.gradle
- Keystore password wrong or keystore corrupted
- Key alias not found in keystore
- Signing config not assigned to release buildType

## Fixes

- Verify keystore path and password
- Check key alias with keytool -list
- Assign signingConfigs to buildTypes
- Store keystore securely, not in version control

## Code Example

```kotlin
android {
    signingConfigs {
        release {
            storeFile file("keystore.jks")
            storePassword System.getenv("KEYSTORE_PASSWORD") ?: ""
            keyAlias System.getenv("KEY_ALIAS") ?: ""
            keyPassword System.getenv("KEY_PASSWORD") ?: ""
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
        }
    }
}
```

# List keystore contents:
keytool -list -v -keystore keystore.jks
# Never commit keystore or passwords to git
