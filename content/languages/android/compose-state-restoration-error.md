---
title: "State Restoration Error"
description: "Fix Compose state restoration and process death recovery errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose state is lost after process death or configuration change

## Common Causes

- rememberSaveable not saving complex objects
- Bundle serialization failing for custom types
- State not restored after process death
- ViewModel state not persisting through SavedStateHandle

## Fixes

- Use rememberSaveable with Saver for custom types
- Implement Parcelable for complex state objects
- Use SavedStateHandle in ViewModel
- Test process death with adb shell am kill

## Code Example

```kotlin
// Process death recovery
@Composable
fun MyScreen(viewModel: MyViewModel = hViewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    // State survives process death via SavedStateHandle
}

// Manual state restoration:
var text by rememberSaveable { mutableStateOf("") }

// Custom type restoration:
val dataSaver = Saver<CustomData, Bundle>(
    save = { bundleOf("key" to it.value) },
    restore = { CustomData(it.getString("key") ?: "") }
)
var data by rememberSaveable(stateSaver = dataSaver) {
    mutableStateOf(CustomData("default"))
}
```

# rememberSaveable: survives process death
# SavedStateHandle: ViewModel state survival
# Parcelable: complex object serialization
# Test with: adb shell am kill com.example.app
