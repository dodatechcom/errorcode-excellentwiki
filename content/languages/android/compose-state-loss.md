---
title: "Compose State Loss"
description: "Fix state loss errors in Jetpack Compose when navigating or recomposing"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
UI state is lost when navigating away and returning to a Compose screen

## Common Causes

- State not held in ViewModel or remember
- Configuration change resets Compose state
- Navigation popUpTo clears state
- Process death loses all non-saved state

## Fixes

- Use ViewModel to persist state across recompositions
- Use rememberSaveable for config-change survival
- Save critical state in SavedStateHandle
- Use navOptions { launchSingleTop = true }

## Code Example

```kotlin
@Composable
fun MyScreen(viewModel: MyViewModel = hiltViewModel()) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // Or for simple state:
    var text by rememberSaveable { mutableStateOf("") }

    TextField(value = text, onValueChange = { text = it })
}
```

# Use ViewModel for complex state
# Use rememberSaveable for simple state
# Both survive configuration changes
