---
title: "LazyColumn Multi-Select Error"
description: "Fix LazyColumn multi-item selection and selection state management"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn multi-selection not working or selection state not properly tracked

## Common Causes

- Cannot select multiple items
- Selection state lost on scroll
- Select all not working correctly
- Selection not visually indicated

## Fixes

- Track selection with mutableStateListOf
- Visual indication for selected items
- Implement select all/deselect all
- Handle selection during scroll with key

## Code Example

```kotlin
var selectedItems = remember { mutableStateSetOf<String>() }

LazyColumn {
    items(items, key = { it.id }) { item ->
        ListItem(
            modifier = Modifier.toggleable(
                value = selectedItems.contains(item.id),
                onValueChange = {
                    if (selectedItems.contains(item.id)) selectedItems.remove(item.id)
                    else selectedItems.add(item.id)
                }
            )
        )
    }
}
```

# mutableStateSetOf for selection tracking# toggleable modifier for selection toggle# Visual indication for selected state# key for stable selection across scroll
