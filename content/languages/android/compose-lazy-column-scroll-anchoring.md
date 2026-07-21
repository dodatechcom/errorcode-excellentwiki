---
title: "Scroll Anchoring Error"
description: "Fix LazyColumn scroll anchoring and position restoration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn scroll position lost when navigating away and back

## Common Causes

- Scroll position not saved on navigation
- List scrolling to top after configuration change
- Scroll position not restored after process death
- Nested scroll lists conflicting

## Fixes

- Use rememberLazyListState for position preservation
- Save scroll position in ViewModel or SavedStateHandle
- Test scroll preservation across navigation
- Use nested scroll connection for nested lists

## Code Example

```kotlin
// LazyListState automatically saves scroll position
val listState = rememberLazyListState()

LazyColumn(state = listState) {
    items(items) { item -> ItemRow(item) }
}

// Save/restore scroll position in ViewModel:
class MyViewModel(savedStateHandle: SavedStateHandle) : ViewModel() {
    private val scrollPosition = savedStateHandle.getLiveData<Int>("scroll_pos", 0)
    
    fun saveScrollPosition(position: Int) {
        scrollPosition.value = position
    }
}
```

# rememberLazyListState: auto-saves position
# SavedStateHandle: explicit position save
# Test across navigation and config changes
# Nested scroll: use nestedScroll connection
