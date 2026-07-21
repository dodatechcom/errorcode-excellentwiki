---
title: "Firebase Configuration Error"
description: "Fix Firebase configuration and google-services.json errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase services fail to initialize because of missing or incorrect configuration

## Common Causes

- google-services.json not placed in app/ directory
- Package name in google-services.json does not match app
- google-services plugin not applied in build.gradle
- Firebase SDK dependencies not added

## Fixes

- Download google-services.json from Firebase console
- Verify package_name matches applicationId in build.gradle
- Apply google-services plugin in app-level build.gradle
- Add Firebase BOM for version management

## Code Example

```kotlin
// Project-level build.gradle
plugins {
    id 'com.google.gms.google-services' version '4.4.0' apply false
}

// App-level build.gradle
plugins {
    id 'com.google.gms.google-services'
}

dependencies {
    implementation platform('com.google.firebase:firebase-bom:32.7.0')
    implementation 'com.google.firebase:firebase-analytics'
    implementation 'com.google.firebase:firebase-auth'
}
```

# google-services.json must be in app/ directory
# Verify package name: grep package google-services.json
# Verify applicationId matches in build.gradle
