---
title: "Hilt Assisted Injection Error"
description: "Fix Hilt assisted injection and @AssistedInject configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Hilt cannot create objects that require both injected and runtime parameters

## Common Causes

- @AssistedInject constructor not properly annotated
- AssistedFactory not generating implementation
- Runtime parameters not passed through factory
- Factory method not returning correct type

## Fixes

- Use @AssistedInject on constructor with @Assisted params
- Define @AssistedFactory interface
- Pass runtime params through factory method
- Use @AssistedInject.Factory for complex creation

## Code Example

```kotlin
class MyWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    private val repository: Repository  // Injected
) : CoroutineWorker(context, params) {

    @AssistedFactory
    interface Factory {
        fun create(context: Context, params: WorkerParameters): MyWorker
    }

    override suspend fun doWork(): Result {
        repository.sync()
        return Result.success()
    }
}

// Usage with HiltWorkerFactory:
val work = OneTimeWorkRequestBuilder<MyWorker>().build()
WorkManager.getInstance(context).enqueue(work)
```

# @AssistedInject: mix of injected and runtime params
# @Assisted: marks runtime parameters
# @AssistedFactory: creates instances with runtime params
