---
title: "Plugins Block Error"
description: "Fix errors in the plugins block of Android Gradle build files"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
The plugins {} block in build.gradle contains invalid configuration

## Common Causes

- Plugin ID not declared in settings.gradle pluginManagement
- Version not specified when required
- apply false missing for library plugins
- Plugin artifact not found in configured repositories

## Fixes

- Add plugin repository to settings.gradle pluginManagement
- Specify plugin version explicitly
- Use apply false for non-app modules
- Check plugin artifact availability

## Code Example

```kotlin
// settings.gradle
pluginManagement {
    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
    }
}
// build.gradle
plugins {
    id 'com.android.application' version '8.2.0' apply false
}
```

# Ensure pluginManagement is in settings.gradle
# before the plugins block in build.gradle
