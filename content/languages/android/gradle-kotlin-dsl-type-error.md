---
title: "Kotlin DSL Type Error"
description: "Fix type errors in Gradle Kotlin DSL build scripts for Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build script fails with type mismatch in Gradle Kotlin DSL configuration

## Common Causes

- Using Groovy syntax in Kotlin DSL files
- Missing type casts for extension properties
- Incompatible plugin DSL syntax
- Incorrect lambda syntax for configuration blocks

## Fixes

- Use Kotlin DSL assignment syntax with = operator
- Add explicit type when needed
- Reference extensions with proper Kotlin types
- Use configure<ExtensionType> for custom extensions

## Code Example

```kotlin
// Wrong (Groovy syntax):
android.compileSdkVersion 34
// Correct (Kotlin DSL):
android.compileSdk = 34

// Or with configure:
configure<BaseAppModuleExtension> {
    compileSdk = 34
}
```

# Convert Groovy to Kotlin DSL:
# Replace single quotes with double quotes
# Use = for assignment
# Use named arguments for method calls
