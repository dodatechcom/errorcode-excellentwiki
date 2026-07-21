---
title: "Flow Collection Error"
description: "Fix Kotlin Flow collection errors in Android ViewModel and Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Flow does not emit values or collection is cancelled prematurely

## Common Causes

- collect called on wrong dispatcher
- Flow collected outside lifecycle scope
- StateFlow not emitting initial value
- SharedFlow replay not configured for new subscribers

## Fixes

- Use collectAsStateWithLifecycle in Compose
- Collect flow in lifecycleScope.launch
- Use StateFlow with initial value for UI state
- Configure SharedFlow replay if needed

## Code Example

```kotlin
// WRONG: collect not lifecycle-aware
lifecycleScope.launch {
    flow.collect { updateUI(it) }  // Continues in background
}

// CORRECT: lifecycle-aware collection
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        flow.collect { updateUI(it) }
    }
}

// In Compose:
val state by viewModel.uiState.collectAsStateWithLifecycle()
```

# collectAsStateWithLifecycle() for Compose
# repeatOnLifecycle() for XML activities
# Both pause collection when not visible
