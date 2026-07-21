---
title: "WorkManager Worker Error"
description: "Fix WorkManager Worker class implementation errors and doWork failures"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Worker fails to execute or returns incorrect Result

## Common Causes

- doWork() not returning Result.success/failure/retry
- Worker class not properly constructed
- Worker not registered with WorkManager
- InputData not received correctly

## Fixes

- Return appropriate Result from doWork()
- Worker must have public constructor with Context and WorkerParameters
- Use WorkManager.enqueue() to schedule work
- Use inputData to pass parameters to Worker

## Code Example

```kotlin
class UploadWorker(
    context: Context,
    params: WorkerParameters
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        val fileUri = inputData.getString("file_uri")
            ?: return Result.failure()

        return try {
            uploadFile(fileUri)
            Result.success()
        } catch (e: IOException) {
            Result.retry()
        }
    }
}

// Enqueue with input:
val data = workDataOf("file_uri" to uri.toString())
val work = OneTimeWorkRequestBuilder<UploadWorker>()
    .setInputData(data)
    .build()
```

# Use CoroutineWorker for async work
# Use Worker for synchronous work
# Return Result.retry() for transient failures
