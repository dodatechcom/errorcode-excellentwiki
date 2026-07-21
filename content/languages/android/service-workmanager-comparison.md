---
title: "Service vs WorkManager Decision Guide"
description: "When to use Android Service vs WorkManager vs JobScheduler"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Confusion about whether to use Service, WorkManager, or JobScheduler for background work

## Common Causes

- Using Service for work that should survive process death
- Using WorkManager for real-time high-priority work
- Using JobScheduler instead of WorkManager for simplicity
- Long-running work without proper lifecycle management

## Fixes

- Use Service for immediate foreground work
- Use WorkManager for deferrable guaranteed work
- Use Foreground Service for long-running visible work
- Use WorkManager with constraints for network-dependent tasks

## Code Example

```kotlin
// Foreground Service: immediate, long-running, user-visible
class MusicService : Service() { ... }

// WorkManager: guaranteed, deferred, constraints
val uploadWork = OneTimeWorkRequestBuilder<UploadWorker>()
    .setConstraints(constraints)
    .build()
WorkManager.getInstance(context).enqueue(uploadWork)

// CoroutineScope: lightweight background work
viewModelScope.launch(Dispatchers.IO) {
    repository.syncData()
}
```

# Service: continuous work (music, downloads)
# WorkManager: guaranteed execution (uploads, sync)
# Foreground Service: user-visible long work
# Coroutine: lightweight, lifecycle-aware
