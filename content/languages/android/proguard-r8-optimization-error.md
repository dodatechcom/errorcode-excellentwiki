---
title: "R8 Optimization Error"
description: "Fix R8 optimization errors that break Android app behavior"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
R8 code optimization changes program behavior causing unexpected crashes

## Common Causes

- R8 inlines too aggressively removing interfaces
- Enum optimization breaks ordinal-based logic
- Static field initialization order changed
- Class hierarchy flattened incorrectly

## Fixes

- Disable specific R8 optimizations with -optimizations
- Keep enum classes unoptimized
- Test release builds throughout development
- Use dontoptimize for sensitive code paths

## Code Example

```kotlin
# Disable specific optimizations
-optimizations !code/simplification/variable,!code/simplification/assignment
-optimizationpasses 5

# Keep enums intact
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}
```

# Run R8 with verbose output to see optimizations
./gradlew assembleRelease --info
# Check mapping.txt for changes
