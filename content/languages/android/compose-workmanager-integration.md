---
title: "Compose WorkManager Integration Error"
description: "Fix Compose and WorkManager integration for background task observation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WorkManager state not properly observed in Compose UI

## Common Causes

- Work info not being observed in Compose
- Work state not triggering recomposition
- Worker result not displayed in UI
- Work request not unique and duplicates running

## Fixes

- Use workManager.getWorkInfosByTagLiveData in Compose
- Observe with collectAsStateWithLifecycle
- Use unique work names for deduplication
- Show work status in UI with state-based rendering

## Code Example

```kotlin
@Composable
fun SyncStatusScreen(workManager: WorkManager) {
    val workInfos by workManager
        .getWorkInfosByTagLiveData("sync")
        .collectAsStateWithLifecycle(initialValue = emptyList())

    val currentWork = workInfos.firstOrNull()

    when (currentWork?.state) {
        WorkInfo.State.RUNNING -> CircularProgressIndicator()
        WorkInfo.State.SUCCEEDED -> Text("Sync complete")
        WorkInfo.State.FAILED -> Text("Sync failed")
        WorkInfo.State.ENQUEUED -> Text("Waiting to sync")
        else -> Text("No sync in progress")
    }
}
```

# getWorkInfosByTagLiveData: observe by tag
# collectAsStateWithLifecycle: lifecycle-aware
# Show work state based on WorkInfo.State
