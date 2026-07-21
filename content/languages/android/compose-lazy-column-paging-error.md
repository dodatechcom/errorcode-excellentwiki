---
title: "LazyColumn Paging Error"
description: "Fix LazyColumn infinite scroll and paging implementation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn does not trigger load-more when scrolling near bottom

## Common Causes

- Scroll to bottom not detected
- Load-more triggered multiple times
- Paging state not properly managed
- Last item not triggering load

## Fixes

- Detect scroll to bottom with scrollState
- Debounce or guard against multiple triggers
- Manage paging state in ViewModel
- Use derivedStateOf for scroll detection

## Code Example

```kotlin
val listState = rememberLazyListState()

LazyColumn(state = listState) {
    items(list, key = { it.id }) { item ->
        ItemRow(item)
    }
}

// Detect scroll to bottom
val shouldLoadMore by remember {
    derivedStateOf {
        val lastVisibleItem = listState.layoutInfo.visibleItemsInfo.lastOrNull()?.index ?: 0
        val totalItems = listState.layoutInfo.totalItemsCount
        lastVisibleItem >= totalItems - 3 && !isLoadingMore && hasMorePages
    }
}

LaunchedEffect(shouldLoadMore) {
    if (shouldLoadMore) {
        onLoadMore()
    }
}
```

# Detect scroll position with layoutInfo
# derivedStateOf for efficient detection
# Guard against multiple triggers
# Manage paging state in ViewModel
