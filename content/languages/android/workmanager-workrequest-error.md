---
title: "WorkManager WorkRequest Error"
description: "Fix WorkManager WorkRequest configuration and scheduling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkRequest not configured correctly causing work not to schedule

## Common Causes

- WorkRequest not unique and duplicates created
- Periodic work interval too short (minimum 15 minutes)
- Existing work policy conflicts with new request
- Work tag not set for later cancellation

## Fixes

- Use ExistingWorkPolicy to handle duplicates
- Set interval >= 15 minutes for periodic work
- Use REPLACE, KEEP, or APPEND policy appropriately
- Tag work for group cancellation

## Code Example

```kotlin
// One-time work with unique constraint
val uploadWork = OneTimeWorkRequestBuilder<UploadWorker>()
    .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)
    .addTag("upload")
    .build()

WorkManager.getInstance(context)
    .enqueueUniqueWork(
        "uploadWork",
        ExistingWorkPolicy.REPLACE,
        uploadWork
    )

// Periodic work (minimum 15 min interval)
val periodicWork = PeriodicWorkRequestBuilder<SyncWorker>(
    15, TimeUnit.MINUTES
).build()
```

# Unique work prevents duplicates
# Tags allow cancelling related work
# BackoffPolicy retries with delay on failure
