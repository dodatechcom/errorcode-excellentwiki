---
title: "WorkManager Data Passing Error"
description: "Fix WorkManager input and output data passing errors between chained tasks"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Data passed between WorkManager tasks is lost or corrupted

## Common Causes

- InputData not received in Worker
- OutputData not set before return
- Data type not matching between tasks
- Data size exceeding limits

## Fixes

- Use inputData.getString() with correct key
- Set outputData with Result.success(outputData)
- Ensure data types match across chain
- Keep WorkManager data small, use DB for large data

## Code Example

```kotlin
// Task A: output data
class TaskA : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        val result = "processed_value"
        val outputData = workDataOf("result_key" to result)
        return Result.success(outputData)
    }
}

// Task B: receive input from Task A
class TaskB : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        val input = inputData.getString("result_key")
        // Process input...
        return Result.success()
    }
}

// Chain with data:
val workA = OneTimeWorkRequestBuilder<TaskA>().build()
val workB = OneTimeWorkRequestBuilder<TaskB>().build()
WorkManager.getInstance(context)
    .beginWith(workA)
    .then(workB)
    .enqueue()
```

# workDataOf() creates key-value data bundle
# Input/output keys must match
# Data limited to 10KB total
