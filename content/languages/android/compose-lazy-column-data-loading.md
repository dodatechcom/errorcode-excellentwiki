---
title: "LazyColumn Data Loading Error"
description: "Fix LazyColumn data loading state management with loading, error, and empty states"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn does not properly handle loading, error, and empty states during data fetch

## Common Causes

- Loading state not showing spinner
- Error state not displayed on failure
- Empty state not shown when no data
- Data refresh not working after error

## Fixes

- Manage UI state with sealed class
- Show different content based on state
- Implement pull-to-refresh for manual refresh
- Handle pagination loading states

## Code Example

```kotlin
sealed class ListState {
    object Loading : ListState()
    data class Error(val message: String) : ListState()
    object Empty : ListState()
    data class Success(val items: List<Item>) : ListState()
}

when (val state = viewModel.listState) {
    is ListState.Loading -> CircularProgressIndicator()
    is ListState.Error -> ErrorMessage(state.message)
    is ListState.Empty -> EmptyState()
    is ListState.Success -> LazyColumn { items(state.items) { ItemRow(it) } }
}
```

# Sealed class for UI states# Different content per state# Pull-to-refresh for manual refresh# Handle all states explicitly
