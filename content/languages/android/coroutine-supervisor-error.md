---
title: "Supervisor Job Error"
description: "Fix Kotlin SupervisorJob and supervisorScope errors in structured concurrency"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
One coroutine failure cancels sibling coroutines unexpectedly

## Common Causes

- Regular Job cancels all children on failure
- supervisorScope not used for independent children
- Child coroutine exception propagates to parent
- supervisorJob not set on scope

## Fixes

- Use SupervisorJob() for independent child coroutines
- Use supervisorScope {} for exception isolation
- Set SupervisorJob on ViewModel scope
- Handle child exceptions individually

## Code Example

```kotlin
// WRONG: one failure cancels all
viewModelScope.launch {
    launch { task1() }  // If this fails, task2 also cancelled
    launch { task2() }
}

// CORRECT: supervisorScope isolates failures
viewModelScope.launch {
    supervisorScope {
        launch { task1() }  // Failure does NOT cancel task2
        launch { task2() }
    }
}

// Or with SupervisorJob:
val scope = CoroutineScope(SupervisorJob() + Dispatchers.Main)
```

# Use SupervisorJob when child coroutines are independent
# Use supervisorScope {} for structured isolation
# Handle each child's exceptions separately
