---
title: "WorkManager Constraint Compatibility Error"
description: "Fix WorkManager constraint compatibility across different Android API levels"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager constraints behave differently across Android versions

## Common Causes

- BatteryNotLow not working on older devices
- NetworkType.CONNECTED behavior varies
- StorageNotLow not available on API < 23
- Constraints not evaluated on app restore

## Fixes

- Test constraints on multiple API levels
- Use appropriate constraint fallbacks
- Check WorkInfo state for constraint status
- Handle constraint changes with observer

## Code Example

```kotlin
// Check current constraint status:
val workManager = WorkManager.getInstance(context)
val workInfo = workManager.getWorkInfoById(workId).get()
Log.d("Work", "Constraints met: ${workInfo.constraints}")

// Observe constraint changes:
workManager.getWorkInfoByIdLiveData(workId).observe(this) { info ->
    when (info?.state) {
        WorkInfo.State.ENQUEUED -> Log.d("Work", "Waiting for constraints")
        WorkInfo.State.RUNNING -> Log.d("Work", "Running")
        else -> {}
    }
}
```

# Constraints evaluated when app is running
# WorkManager does not start work for constraint changes
# Use periodic work for regular checks
