---
title: "WorkManager Constraint Error"
description: "Fix WorkManager worker constraint errors preventing work execution"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager does not execute work because constraints are not met

## Common Causes

- NetworkType constraint not matching current connectivity
- BatteryNotLow constraint preventing execution
- StorageNotLow constraint failing
- RequiresCharging constraint when not plugged in

## Fixes

- Check current constraint status before enqueuing
- Use setRequiresNetworkType for flexible network needs
- Log constraint status in Worker for debugging
- Use setExpedited for time-sensitive work

## Code Example

```kotlin
val constraints = Constraints.Builder()
    .setRequiredNetworkType(NetworkType.CONNECTED)
    .setRequiresBatteryNotLow(true)
    .setRequiresStorageNotLow(true)
    .build()

val uploadWork = OneTimeWorkRequestBuilder<UploadWorker>()
    .setConstraints(constraints)
    .build()

WorkManager.getInstance(context).enqueue(uploadWork)
```

# Check why work is not running:
WorkManager.getInstance(context)
    .getWorkInfoByIdLiveData(workId)
    .observe(this) { workInfo ->
        Log.d("Work", "State: ${workInfo?.state}")
        Log.d("Work", "Constraints: ${workInfo?.constraints}")
    }
