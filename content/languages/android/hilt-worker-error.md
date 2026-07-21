---
title: "Hilt Worker Error"
description: "Fix Hilt Worker and WorkManager dependency injection errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Hilt does not inject dependencies into WorkManager Worker classes

## Common Causes

- @HiltWorker annotation missing on Worker class
- Worker not using HiltWorkerFactory
- AssistedInject parameters not provided
- WorkManager not configured for Hilt

## Fixes

- Add @HiltWorker annotation to Worker
- Implement Worker with @AssistedInject constructor
- Configure HiltWorkerFactory in Application
- Use @HiltViewModel for Worker in Compose

## Code Example

```kotlin
@HiltWorker
class SyncWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    private val repository: Repository
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        return try {
            repository.sync()
            Result.success()
        } catch (e: Exception) {
            Result.retry()
        }
    }
}

// Enqueue:
val work = OneTimeWorkRequestBuilder<SyncWorker>().build()
WorkManager.getInstance(context).enqueue(work)
```

# Dependencies:
# implementation 'androidx.hilt:hilt-work:1.1.0'
# kapt 'androidx.hilt:hilt-compiler:1.1.0'
# Must configure HiltWorkerFactory in Application
