---
title: "Unique Work Error"
description: "Fix WorkManager unique work naming and conflict resolution errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Work requests conflict because of duplicate unique work names

## Common Causes

- Same unique work name used for different purposes
- ExistingWorkPolicy not handling duplicates correctly
- Periodic and one-time work sharing name
- Work not cancelled when new request enqueued

## Fixes

- Use unique names per work purpose
- Choose appropriate ExistingWorkPolicy
- Separate periodic and one-time work names
- Use cancelWork by tag or name for cleanup

## Code Example

```kotlin
// REPLACE: cancel existing, run new
WorkManager.getInstance(context)
    .enqueueUniqueWork(
        "uploadSync",
        ExistingWorkPolicy.REPLACE,
        uploadWork
    )

// KEEP: ignore new if existing running
WorkManager.getInstance(context)
    .enqueueUniqueWork(
        "backgroundSync",
        ExistingWorkPolicy.KEEP,
        syncWork
    )

// Periodic: use enqueueUniquePeriodicWork
WorkManager.getInstance(context)
    .enqueueUniquePeriodicWork(
        "periodicSync",
        ExistingPeriodicWorkPolicy.KEEP,
        periodicWork
    )
```

# ExistingWorkPolicy.REPLACE: cancel and replace
# ExistingWorkPolicy.KEEP: keep existing
# ExistingWorkPolicy.APPEND: queue after existing
