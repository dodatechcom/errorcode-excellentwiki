---
title: "API Annotation Error"
description: "Fix @RequiresApi and @SuppressLint annotation errors for API level restrictions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Lint or compiler warns about missing API level annotations

## Common Causes

- @RequiresApi missing on method using newer APIs
- Wrong API level constant in annotation
- Annotation not propagated to callers
- SuppressLint used to suppress required warning

## Fixes

- Add @RequiresApi(Build.VERSION_CODES.X) to method
- Use correct version constant matching API level
- Add annotation to all caller methods too
- Only use @SuppressLint when you have proper fallback

## Code Example

```kotlin
@RequiresApi(Build.VERSION_CODES.S)
fun enableBluetoothPermissions() {
    // API 31+ code here
}

// Callers must also annotate:
@RequiresApi(Build.VERSION_CODES.S)
fun setupBluetooth() {
    enableBluetoothPermissions()
}
```

# Find missing annotations
./gradlew lintDebug | grep "NewApi"
# Add annotation to each flagged method
