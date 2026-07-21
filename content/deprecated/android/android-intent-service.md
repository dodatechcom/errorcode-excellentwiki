---
title: "[Solution] Deprecated Function Migration: IntentService to WorkManager"
description: "Migrate from deprecated IntentService to WorkManager for background work."
deprecated_function: "IntentService"
replacement_function: "WorkManager"
languages: ["kotlin"]
deprecated_since: "Android 11 (API 30)"
---

# [Solution] Deprecated Function Migration: IntentService to WorkManager

The `IntentService` has been deprecated in favor of `WorkManager`.

## Migration Guide

IntentService does not respect Doze mode. WorkManager handles constraints, retries, persistence.

## Before (Deprecated)

```kotlin
public class MyIntentService extends IntentService {
    public MyIntentService() { super("MyIntentService"); }
    @Override
    protected void onHandleIntent(Intent intent) {
        String data = intent.getStringExtra("data");
        processInBackground(data);
    }
}
```

## After (Modern)

```kotlin
class MyWorker(context: Context, params: WorkerParameters) :
    CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        val data = inputData.getString("data") ?: return Result.failure()
        return try {
            processInBackground(data)
            Result.success()
        } catch (e: Exception) {
            Result.retry()
        }
    }
}

val request = OneTimeWorkRequestBuilder<MyWorker>()
    .setInputData(workDataOf("data" to "value"))
    .setConstraints(Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .build())
    .build()
WorkManager.getInstance(context).enqueue(request)
```

## Key Differences

- WorkManager handles Doze mode
- Constraints for network, battery, etc.
- Automatic retries with backoff
- Persistent -- survives app restarts
