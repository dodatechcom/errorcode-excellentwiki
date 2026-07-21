---
title: "ProduceState Error"
description: "Fix Compose produceState and snapshotFlow data loading errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
produceState does not load data correctly or causes composition issues

## Common Causes

- produceState not loading initial value
- Data not updating when source changes
- produceState running on wrong thread
- Initial value not displayed during loading

## Fixes

- Provide initial value to produceState
- Use keys to re-trigger data loading
- Use withContext(Dispatchers.IO) for background work
- Show loading state while data is fetching

## Code Example

```kotlin
val items by produceState<List<Item>>(initialValue = emptyList()) {
    // Loading state is emptyList()
    value = emptyList()

    // Fetch data
    value = try {
        repository.getItems()
    } catch (e: Exception) {
        emptyList()
    }
}

// With key to reload:
val items by produceState(emptyList<Item>(), userId) {
    value = repository.getItemsForUser(userId)
}

// snapshotFlow for state-based side effects:
LaunchedEffect(Unit) {
    snapshotFlow { scrollState.firstVisibleItemIndex }
        .distinctUntilChanged()
        .collect { index -> analytics.logScroll(index) }
}
```

# produceState: coroutine-based state production
# Key changes re-trigger the coroutine
# snapshotFlow: observe Compose state changes
