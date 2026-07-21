---
title: "Compose Scroll Performance Error"
description: "Fix Compose LazyColumn and LazyRow scrolling performance issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn or LazyRow stutters during fast scrolling

## Common Causes

- Items not using stable keys
- Content recomposing on every scroll position
- Heavy computation in item composable
- Missing contentType for item reuse

## Fixes

- Provide stable key parameter
- Use key() for items to prevent unnecessary recomposition
- Keep item composables lightweight
- Set contentType for item recycling

## Code Example

```kotlin
LazyColumn(
    // Performance optimizations
    contentPadding = PaddingValues(16.dp)
) {
    items(
        items = items,
        key = { it.id },  // Stable keys
        contentType = { it.type }  // Item type for recycling
    ) { item ->
        // Lightweight item composable
        ListItem(
            title = item.title,  // String, not composable
            onClick = { onItemClicked(item) }
        )
    }
}
```

# key: stable identity for items
# contentType: helps with item recycling
# Keep items lightweight
# Avoid complex layouts in items
