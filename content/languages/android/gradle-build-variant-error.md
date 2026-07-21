---
title: "Build Variant Error"
description: "Fix Android build variant and flavor configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build variant or product flavor configuration causes build failure

## Common Causes

- Flavor dimension not declared in build.gradle
- Build type not matching variant filter
- Variant not appearing in build menu
- Flavor-specific source set missing

## Fixes

- Declare flavorDimensions in defaultConfig
- Verify build type names match in all modules
- Check variant filter in build.gradle
- Create flavor-specific directories under src/

## Code Example

```kotlin
android {
    flavorDimensions "tier"
    productFlavors {
        free {
            dimension "tier"
            applicationIdSuffix ".free"
        }
        pro {
            dimension "tier"
            applicationIdSuffix ".pro"
        }
    }
}

// Source sets:
// src/free/java/  (free flavor code)
// src/pro/java/   (pro flavor code)
// src/debug/java/ (debug build type)
// src/freeDebug/java/ (combined)
```

# Build variant = flavor + build type
# freeDebug, freeRelease, proDebug, proRelease
# Check variant in Build > Select Variant
