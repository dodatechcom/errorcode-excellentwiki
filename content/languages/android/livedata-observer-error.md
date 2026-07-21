---
title: "LiveData Observer Error"
description: "Fix LiveData observer errors and lifecycle awareness issues in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LiveData observer does not receive updates or receives them on wrong lifecycle state

## Common Causes

- Observer not lifecycle-aware using observeForever
- Observer added in wrong lifecycle state
- setValue called from background thread
- Multiple observers with conflicting updates

## Fixes

- Use lifecycleOwner.observe{} instead of observeForever
- Add observers in onStart or onCreate
- Use postValue from background threads
- Use distinctUntilChanged to filter duplicate values

## Code Example

```kotlin
// CORRECT lifecycle-aware observation
viewModel.uiState.observe(viewLifecycleOwner) { state ->
    when (state) {
        is UiState.Loading -> showLoading()
        is UiState.Success -> showData(state.data)
        is UiState.Error -> showError(state.message)
    }
}

// From background thread:
liveData.postValue(newValue)  // Thread-safe

// From main thread:
liveData.value = newValue
```

# Never use observeForever without manual removal
# Always observe with lifecycleOwner
# Use postValue for background thread updates
