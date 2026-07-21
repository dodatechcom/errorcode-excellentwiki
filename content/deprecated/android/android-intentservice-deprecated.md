---
title: "[Solution] Deprecated Function Migration: IntentService to WorkManager"
description: "Migrate from deprecated IntentService to WorkManager."
deprecated_function: "IntentService"
replacement_function: "WorkManager"
languages: ["android"]
deprecated_since: "Android 11+"
---

# [Solution] Deprecated Function Migration: IntentService to WorkManager

The `IntentService` has been deprecated in favor of `WorkManager`.

## Migration Guide

IntentService was deprecated in API 30.

## Before (Deprecated)

```android
class MyIntentService : IntentService("MyService") {
    override fun onHandleIntent(intent: Intent?) { }
}
```

## After (Modern)

```android
class MyWorker(context: Context, params: WorkerParameters) : Worker(context, params) {
    override fun doWork(): Result {
        return Result.success()
    }
}
```

## Key Differences

- WorkManager handles background work
