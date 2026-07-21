---
title: "Version Code Reference Error"
description: "Fix Android Build.VERSION_CODES usage errors and version constant references"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because referenced Build.VERSION_CODES constant does not exist

## Common Causes

- Typo in version code constant name
- Using future API level constant not yet available
- Wrong constant for intended API level
- Using integer instead of Build.VERSION_CODES constant

## Fixes

- Use exact constant name from Build.VERSION_CODES
- Check Android SDK documentation for available constants
- Match integer API level to correct constant name
- Use Build.VERSION.SDK_INT for runtime checks

## Code Example

```kotlin
// Wrong: using integer
if (Build.VERSION.SDK_INT >= 33) { ... }

// Correct: using constant
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) { ... }

// Common constants:
// TIRAMISU = 33 (Android 13)
// S = 31 (Android 12)
// R = 30 (Android 11)
// Q = 29 (Android 10)
```

# See all version codes:
# android.os.Build.VERSION_CODES
# Or check: developer.android.com/reference/android/os/Build.VERSION_CODES
