---
title: "LazyColumn Item Placement Error"
description: "Fix LazyColumn item placement and spacing with itemPlacement"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items have inconsistent spacing or alignment issues

## Common Causes

- Items not properly aligned to grid
- Spacing between items inconsistent
- First and last items have different margins
- Item heights not consistent

## Fixes

- Use itemSpacing for consistent spacing
- Use contentPadding for outer margins
- Set fixed heights for consistent sizing
- Use Arrangement for alignment

## Code Example

```kotlin
LazyColumn(
    contentPadding = PaddingValues(horizontal = 16.dp, vertical = 8.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp)
) {
    items(items, key = { it.id }) { item ->
        Card(
            modifier = Modifier.fillMaxWidth(),
            shape = RoundedCornerShape(12.dp)
        ) {
            ListItem(item)
        }
    }
}
```

# contentPadding: outer padding
# verticalArrangement.spacedBy: item spacing
# item { } for headers/footers
# items() for list items
