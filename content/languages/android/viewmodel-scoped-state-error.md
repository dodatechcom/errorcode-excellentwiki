---
title: "ViewModel State Error"
description: "Fix ViewModel state management errors and state loss in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewModel state is lost or not properly updated when UI recreates

## Common Causes

- State not held in ViewModel or wrong scope
- MutableState updated from wrong coroutine scope
- StateFlow not collected with lifecycle awareness
- Configuration change creates new ViewModel instance

## Fixes

- Store UI state in ViewModel using StateFlow
- Update state with viewModelScope.launch
- Collect with collectAsStateWithLifecycle()
- Use viewModel() delegate to share ViewModel

## Code Example

```kotlin
class MyViewModel : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    fun loadData() {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val data = repository.fetch()
                _uiState.value = UiState.Success(data)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message)
            }
        }
    }
}

// In Composable:
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

# StateFlow survives configuration changes
# collectAsStateWithLifecycle pauses when not visible
# Use SavedStateHandle for process death survival
