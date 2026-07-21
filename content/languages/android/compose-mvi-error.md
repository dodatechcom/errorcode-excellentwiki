---
title: "Compose MVI Error"
description: "Fix MVI pattern implementation errors in Jetpack Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
MVI pattern does not properly handle state, intent, and side effects

## Common Causes

- State not sealed class covering all cases
- Intent not dispatched to ViewModel correctly
- Side effect not consumed exactly once
- State not properly reduced after intent

## Fixes

- Define sealed class for UI State with Loading/Success/Error
- Use Channel for one-time events
- Collect state with collectAsStateWithLifecycle
- Handle each intent in ViewModel when block

## Code Example

```kotlin
// State
sealed class UiState {
    data object Loading : UiState()
    data class Success(val items: List<Item>) : UiState()
    data class Error(val message: String) : UiState()
}

// Intent
sealed class UiIntent {
    data class LoadItems(val page: Int) : UiIntent()
    data class DeleteItem(val id: Long) : UiIntent()
}

// ViewModel
class MyViewModel : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    fun handleIntent(intent: UiIntent) {
        when (intent) {
            is UiIntent.LoadItems -> loadItems(intent.page)
            is UiIntent.DeleteItem -> deleteItem(intent.id)
        }
    }
}
```

# MVI: Model-View-Intent pattern
# State: immutable UI state
# Intent: user actions
# SideEffect: one-time events
