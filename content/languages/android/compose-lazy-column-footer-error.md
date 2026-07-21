---
title: "LazyColumn Footer Error"
description: "Fix LazyColumn footer and load-more pagination indicator errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn footer does not show loading indicator or load-more trigger fails

## Common Causes

- Footer not appearing at end of list
- Load-more not triggering on scroll to bottom
- Loading indicator blocking user interaction
- Multiple load-more triggers firing

## Fixes

- Add footer item after list items
- Use LaunchedEffect to detect scroll end
- Show loading indicator only when loading
- Debounce load-more triggers

## Code Example

```kotlin
LazyColumn {
    items(list, key = { it.id }) { item ->
        ItemRow(item)
    }
    
    // Footer with loading indicator
    if (isLoadingMore) {
        item {
            Box(
                modifier = Modifier.fillMaxWidth().padding(16.dp),
                contentAlignment = Alignment.Center
            ) {
                CircularProgressIndicator()
            }
        }
    }
    
    // Load more trigger
    item {
        LaunchedEffect(Unit) {
            if (list.isNotEmpty() && !isLoadingMore) {
                onLoadMore()
            }
        }
    }
}
```

# Footer item for loading indicator
# LaunchedEffect for load-more trigger
# Debounce to prevent multiple triggers
# Show/hide based on loading state
