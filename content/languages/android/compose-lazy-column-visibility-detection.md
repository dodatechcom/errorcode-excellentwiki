---
title: "LazyColumn Visibility Detection Error"
description: "Fix LazyColumn item visibility detection and viewport tracking"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Cannot detect when specific items are visible in LazyColumn viewport

## Common Causes

- Item visibility not detectable
- Viewport items not tracked correctly
- First/last visible item not accessible
- Visibility changes not triggering callbacks

## Fixes

- Use layoutInfo.visibleItemsInfo for viewport items
- Check firstVisibleItemIndex for scroll position
- Use snapshotFlow for reactive visibility tracking
- Track items entering/leaving viewport

## Code Example

```kotlin
val listState = rememberLazyListState()

// Get visible items
val visibleItems = listState.layoutInfo.visibleItemsInfo.map { it.key }

// Detect first visible item
val firstVisibleIndex = listState.firstVisibleItemIndex

// React to visibility changes:
LaunchedEffect(listState) {
    snapshotFlow { listState.firstVisibleItemIndex }
        .distinctUntilChanged()
        .collect { index ->
            analytics.logItemVisible(items[index])
        }
}
```

# layoutInfo.visibleItemsInfo: all visible items
# firstVisibleItemIndex: first visible item position
# snapshotFlow: reactive visibility tracking
# Log analytics when items become visible
