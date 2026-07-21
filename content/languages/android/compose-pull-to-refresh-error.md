---
title: "Compose Pull to Refresh Error"
description: "Fix Compose pull-to-refresh implementation and state management"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Pull-to-refresh does not trigger or refresh indicator not showing

## Common Causes

- PullToRefreshBox not properly configured
- Refresh state not managed correctly
- Content not scrolling to trigger refresh
- Indicator not showing during refresh

## Fixes

- Use PullToRefreshBox from Material 3
- Manage isRefreshing state in ViewModel
- Connect to LazyColumn for scroll trigger
- Show indicator during refresh operation

## Code Example

```kotlin
var isRefreshing by remember { mutableStateOf(false) }

PullToRefreshBox(
    isRefreshing = isRefreshing,
    onRefresh = {
        isRefreshing = true
        viewModel.refresh { isRefreshing = false }
    }
) {
    LazyColumn {
        items(items) { item ->
            ListItem(item)
        }
    }
}
```

# PullToRefreshBox: Material 3 pull to refresh
# isRefreshing: show/hide indicator
# onRefresh: trigger refresh action
# Connect to LazyColumn for scroll support
