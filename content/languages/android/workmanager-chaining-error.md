---
title: "WorkManager Chaining Error"
description: "Fix WorkManager task chaining and parallel execution errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager task chain does not execute in correct order or parallelism is wrong

## Common Causes

- then() called after beginWith() causing wrong order
- Parallel work not properly grouped
- Chain input data not flowing between tasks
- Existing work policy conflicting with new chain

## Fixes

- Use beginWith() for starting parallel work
- Use then() for sequential execution after parallel
- Pass data via setOutputData and inputData
- Use unique work names to avoid conflicts

## Code Example

```kotlin
// Parallel then sequential
val downloadA = OneTimeWorkRequestBuilder<DownloadA>().build()
val downloadB = OneTimeWorkRequestBuilder<DownloadB>().build()
val process = OneTimeWorkRequestBuilder<ProcessData>().build()

WorkManager.getInstance(context)
    .beginWith(listOf(downloadA, downloadB))  // Parallel
    .then(process)  // Sequential after both complete
    .enqueue()

// Chain with data passing:
val workA = OneTimeWorkRequestBuilder<WorkA>().build()
val workB = OneTimeWorkRequestBuilder<WorkB>().build()

WorkManager.getInstance(context)
    .beginWith(workA)
    .then(workB)
    .enqueue()
```

# beginWith: starting point (parallel if list)
# then: runs after previous completes
# Data flows through chain automatically
