---
title: "LazyColumn Arrangement Error"
description: "Fix LazyColumn arrangement, spacing, and alignment errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items are not properly spaced or aligned

## Common Causes

- Items touching edges without padding
- Spacing not consistent between items
- Last item cut off by bottom navigation
- Header and footer not aligned with content

## Fixes

- Use contentPadding for outer padding
- Use verticalArrangement for item spacing
- Account for system bars and navigation
- Use item { } for header and footer

## Code Example

```kotlin
LazyColumn(
    contentPadding = PaddingValues(
        top = 16.dp,
        bottom = 80.dp,  // Space for bottom nav
        start = 16.dp,
        end = 16.dp
    ),
    verticalArrangement = Arrangement.spacedBy(8.dp)
) {
    item {
        Text("Header", style = MaterialTheme.typography.headlineMedium)
    }
    items(items, key = { it.id }) { item ->
        ListItem(item)
    }
    item {
        Spacer(modifier = Modifier.height(16.dp))
    }
}
```

# contentPadding: outer padding around all items
# verticalArrangement: space between items
# item { } for non-list items like headers
