---
title: "Gradle Build Failed -- Compilation Error"
description: "Resolve Gradle build failed compilation errors in Android projects"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails during compilation phase with errors in source code

## Common Causes

- Syntax errors in Java or Kotlin files
- Missing imports or class references
- Type mismatch or incompatible types
- Deprecated API usage without migration

## Fixes

- Review compiler error messages line by line
- Fix syntax errors and missing imports
- Update deprecated API calls
- Clean and rebuild project

## Code Example

```kotlin
// Example: Type mismatch
val num: Int = "hello"  // Error: Type mismatch
// Fix:
val num: Int = 42
```

# Build with detailed output
./gradlew assembleDebug --stacktrace
# Fix each error reported, then rebuild
