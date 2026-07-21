---
title: "WorkManager Tag Error"
description: "Fix WorkManager work tagging and group management errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager work cannot be found, cancelled, or queried by tag

## Common Causes

- Tag not added to WorkRequest
- Tag name not unique across work types
- Querying work by wrong tag
- Cancel by tag not cancelling expected work

## Fixes

- Add tag with addTag() on WorkRequest
- Use consistent tag naming convention
- Use getWorkInfosByTagLiveData for queries
- Verify tag matches before cancelling

## Code Example

```kotlin
// Add tags to work:
val uploadWork = OneTimeWorkRequestBuilder<UploadWorker>()
    .addTag("upload")
    .addTag("network")
    .build()

// Query by tag:
WorkManager.getInstance(context)
    .getWorkInfosByTagLiveData("upload")
    .observe(this) { workInfos ->
        workInfos?.forEach { info ->
            Log.d("Work", "Upload: ${info.state}")
        }
    }

// Cancel by tag:
WorkManager.getInstance(context).cancelAllWorkByTag("upload")

// Cancel by unique name:
WorkManager.getInstance(context).cancelUniqueWork("uniqueUpload")
```

# Tags for grouping and querying
# Unique names for preventing duplicates
# cancelAllWorkByTag: cancel all with tag
