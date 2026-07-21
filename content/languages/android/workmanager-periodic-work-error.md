---
title: "Periodic Work Error"
description: "Fix WorkManager periodic work scheduling and rescheduling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Periodic work stops running or is not rescheduled after device reboot

## Common Causes

- Periodic work not surviving device reboot
- Minimum interval of 15 minutes not respected
- Work not restarted after app update
- Periodic work not respecting constraints

## Fixes

- Use setInitialDelay for first execution timing
- WorkManager auto-reschedules periodic work
- Constraints are re-evaluated each period
- Use OneTimeWork for reboot-triggered work

## Code Example

```kotlin
val periodicWork = PeriodicWorkRequestBuilder<SyncWorker>(
    15, TimeUnit.MINUTES
)
    .setConstraints(Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .build())
    .build()

WorkManager.getInstance(context)
    .enqueueUniquePeriodicWork(
        "periodicSync",
        ExistingPeriodicWorkPolicy.KEEP,
        periodicWork
    )
```

# Periodic work minimum: 15 minutes
# Periodic work auto-reschedules
# Use KEEP to avoid duplicate periodic work
