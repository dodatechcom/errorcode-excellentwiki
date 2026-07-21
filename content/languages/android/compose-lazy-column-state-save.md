---
title: "LazyColumn State Save Error"
description: "Fix LazyColumn scroll state saving and restoration across configuration changes"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn scroll position lost after configuration change or navigation

## Common Causes

- Scroll position not saved automatically
- Configuration change resetting scroll
- Navigation causing scroll to top
- Process death losing scroll position

## Fixes

- Use rememberLazyListState for auto-save
- Save position in ViewModel for persistence
- Use saveState/restoreState for navigation
- Test scroll preservation thoroughly

## Code Example

```kotlin
// LazyListState auto-saves scroll position
val listState = rememberLazyListState()

LazyColumn(state = listState) {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}

// For explicit save/restore:
val savedScrollPosition = rememberSaveable { mutableStateOf(0) }

LaunchedEffect(listState) {
    snapshotFlow { listState.firstVisibleItemIndex }
        .collect { savedScrollPosition.value = it }
}
```

# rememberLazyListState: auto-saves position
# rememberSaveable: explicit position save
# Test across config changes and navigation
# ViewModel for complex state persistence
