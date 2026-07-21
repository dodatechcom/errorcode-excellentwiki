---
title: "Multi-Module Build Error"
description: "Fix Android multi-module Gradle project configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Multi-module Android project fails to build because of module dependency issues

## Common Causes

- Module not declared in settings.gradle
- Circular dependency between modules
- Wrong dependency configuration used
- Module not inheriting common build configuration

## Fixes

- Include all modules in settings.gradle
- Break circular dependencies with interface modules
- Use api for transitive, implementation for internal
- Use convention plugins for shared configuration

## Code Example

```kotlin
// settings.gradle
include ':app'
include ':core'
include ':feature-login'
include ':feature-home'

// app/build.gradle
dependencies {
    implementation project(':core')
    implementation project(':feature-login')
    implementation project(':feature-home')
}

// core/build.gradle
plugins {
    id 'com.android.library'  // Library module
}
```

# Module types:
# - app: main application module
# - library: reusable code module
# - feature: feature-specific module
# - core: shared utilities module
