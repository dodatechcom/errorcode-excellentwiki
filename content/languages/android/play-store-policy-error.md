---
title: "Play Store Policy Error"
description: "Fix Google Play Store policy compliance errors for app submission"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App rejected from Play Store because of policy violations

## Common Causes

- Data safety section not properly filled
- Permission declarations missing or incorrect
- Target API level too old
- Privacy policy not accessible

## Fixes

- Complete Data safety section accurately
- Declare all permissions in Play Console
- Target latest stable API level
- Host accessible privacy policy URL

## Code Example

```kotlin
// Play Console requirements:
// 1. Data safety questionnaire
// 2. Privacy policy URL
// 3. Target API level >= current - 1
// 4. Accurate permission declarations

// In build.gradle:
android {
    defaultConfig {
        targetSdk = 34  // Must be current - 1 at minimum
    }
}
```

# Review Play Console policy center
# Complete Data safety section
# Host privacy policy at accessible URL
# Target latest stable API level
