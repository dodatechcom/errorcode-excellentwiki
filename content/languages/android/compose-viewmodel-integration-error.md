---
title: "Compose ViewModel Integration Error"
description: "Fix Compose and ViewModel integration errors with state collection"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewModel state not properly collected in Compose causing stale or wrong data

## Common Causes

- collectAsState not lifecycle-aware
- StateFlow not emitting latest value
- ViewModel scope not matching Compose lifecycle
- Configuration change losing ViewModel state

## Fixes

- Use collectAsStateWithLifecycle for lifecycle-aware collection
- Use StateFlow for UI state
- Use viewModels() or hiltViewModel() for scoped ViewModel
- Collect state in composable, not LaunchedEffect

## Code Example

```kotlin
@Composable
fun MyScreen(viewModel: MyViewModel = viewModels()) {
    // CORRECT: lifecycle-aware collection
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // WRONG: not lifecycle-aware
    // val uiState by viewModel.uiState.collectAsState()

    when (uiState) {
        is UiState.Loading -> CircularProgressIndicator()
        is UiState.Success -> Content(uiState.data)
        is UiState.Error -> ErrorScreen(uiState.message)
    }
}
```

# collectAsStateWithLifecycle: lifecycle-aware
# collectAsState: not lifecycle-aware
# Use viewModel for state management
# Collect in composable body
