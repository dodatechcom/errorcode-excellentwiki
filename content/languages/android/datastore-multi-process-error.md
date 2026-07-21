---
title: "DataStore Multi-Process Error"
description: "Fix DataStore multi-process access and data corruption errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DataStore data corrupted when accessed from multiple processes

## Common Causes

- DataStore not designed for multi-process access
- Two processes writing same file simultaneously
- File lock not properly implemented
- WorkManager running in different process

## Fixes

- Use single process for DataStore access
- Use ContentProvider for cross-process data
- Ensure all components run in same process
- Use DataStore only for single-process apps

## Code Example

```kotlin
<!-- AndroidManifest.xml: ensure single process -->
<application android:process=":main">
    <!-- All components in same process -->
</application>

// Or use ContentProvider for cross-process:
class DataProvider : ContentProvider() {
    override fun call(method: String, arg: String?, extras: Bundle?): Bundle? {
        return when (method) {
            "getData" -> bundleOf("value" to getDataSync())
            "setData" -> { setDataSync(extras?.getString("value")); null }
            else -> null
        }
    }
}
```

# DataStore is NOT thread-safe across processes
# Use SharedPreferences with MODE_MULTI_PROCESS (deprecated)
# Or use ContentProvider for cross-process data
