---
title: "Work Continuation Chain Error"
description: "Fix WorkManager WorkContinuation chain errors for sequential work execution"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager chain of work requests fails or runs out of order

## Common Causes

- then() called on wrong WorkContinuation
- Parallel work not using then() correctly
- Chain has cycles or invalid dependencies
- InputData not passed through chain

## Fixes

- Use then() to chain sequential work
- Use beginWith() for parallel starting work
- Ensure chain is linear without cycles
- Pass output of one work to next as input

## Code Example

```kotlin
// Sequential chain
val workA = OneTimeWorkRequestBuilder<WorkA>().build()
val workB = OneTimeWorkRequestBuilder<WorkB>().build()
val workC = OneTimeWorkRequestBuilder<WorkC>().build()

WorkManager.getInstance(context)
    .beginWith(workA)
    .then(workB)
    .then(workC)
    .enqueue()

// Parallel then sequential
val parallelWork = listOf(workA, workB)  // Runs in parallel
WorkManager.getInstance(context)
    .beginWith(parallelWork)  // Both start
    .then(workC)  // Runs after both complete
    .enqueue()
```

# WorkContinuation chains outputs
# Use setInputData with workDataOf() to pass data
# Check workInfo.outputData in subsequent workers
