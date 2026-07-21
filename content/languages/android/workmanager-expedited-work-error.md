---
title: "Expedited Work Error"
description: "Fix WorkManager expedited work configuration and foreground requirements"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Expedited work request fails because of foreground service requirements

## Common Causes

- setExpedited not available in newer WorkManager
- Expedited work requires foreground notification
- Expedited work not guaranteed on all devices
- ForegroundInfo not properly configured

## Fixes

- Use setExpedited(OutOfQuotaPolicy.RUN_AS_NON_EXPEDITED_WORK_REQUEST)
- Provide valid notification for foreground info
- Expedited is best-effort, not guaranteed
- Use OneTimeWorkRequest for expedited work

## Code Example

```kotlin
val expeditedWork = OneTimeWorkRequestBuilder<ExpeditedWorker>()
    .setExpedited(OutOfQuotaPolicy.RUN_AS_NON_EXPEDITED_WORK_REQUEST)
    .build()

WorkManager.getInstance(context).enqueueUniqueWork(
    "expeditedSync",
    ExistingWorkPolicy.REPLACE,
    expeditedWork
)

// Worker must call setForeground:
class ExpeditedWorker(context: Context, params: WorkerParameters) :
    CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        setForeground(createForegroundInfo())
        // Do work...
        return Result.success()
    }
}
```

# setExpedited: runs quickly but not guaranteed
# OutOfQuotaPolicy: what to do if quota exceeded
# Must provide ForegroundInfo for expedited work
