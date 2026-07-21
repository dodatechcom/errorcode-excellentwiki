---
title: "ANR Main Thread Error"
description: "Fix Android ANR (Application Not Responding) errors from main thread blocking"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App shows ANR dialog because main thread is blocked for too long

## Common Causes

- Heavy computation on main thread
- Network request on main thread
- Disk I/O on main thread
- Database query on main thread

## Fixes

- Move all I/O to Dispatchers.IO
- Use coroutines for background work
- Use WorkManager for guaranteed background tasks
- Profile with StrictMode to find violations

## Code Example

```kotlin
// WRONG: blocks main thread
val result = apiCall()  // Network on main!

// CORRECT: coroutine with IO dispatcher
viewModelScope.launch(Dispatchers.IO) {
    val result = apiCall()
    withContext(Dispatchers.Main) {
        updateUI(result)
    }
}

// StrictMode to detect violations:
StrictMode.setThreadPolicy(
    StrictMode.ThreadPolicy.Builder()
        .detectAll()
        .penaltyLog()
        .build()
)
```

# ANR threshold: 5 seconds for broadcast
# 10 seconds for service, 20 seconds for broadcast
# Use StrictMode in debug to catch violations
