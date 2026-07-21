---
title: "State Persistence Error"
description: "Fix Compose state persistence across process death and configuration changes"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose state is lost after process death or configuration change

## Common Causes

- rememberSaveable not saving all state
- Complex objects not surviving process death
- ViewModel state not persisting
- Configuration change losing scroll position

## Fixes

- Use rememberSaveable for simple types
- Use SavedStateHandle in ViewModel
- Save scroll position with rememberSaveable
- Test process death recovery

## Code Example

```kotlin
// Simple state survives process death
var text by rememberSaveable { mutableStateOf("") }

// Scroll position survives
val listState = rememberLazyListState()
// listState automatically saves scroll position

// ViewModel with SavedStateHandle:
class MyViewModel(
    savedStateHandle: SavedStateHandle
) : ViewModel() {
    private val query = savedStateHandle.getLiveData<String>("query", "")
    
    fun saveQuery(q: String) {
        savedStateHandle["query"] = q
    }
}
```

# rememberSaveable: survives process death
# ViewModel + SavedStateHandle: complex state
# LazyListState: auto-saves scroll position
# Test: adb shell am kill com.example.app
