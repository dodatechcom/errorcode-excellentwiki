---
title: "LazyColumn Accessible Scroll Error"
description: "Fix LazyColumn accessibility for screen reader scrolling and navigation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn not properly accessible with screen readers for scrolling

## Common Causes

- Screen reader cannot scroll LazyColumn
- Items not announced correctly
- Scroll actions not triggered by accessibility
- Collection semantics not defined

## Fixes

- Provide collection semantics for LazyColumn
- Use semantic properties on items
- Test with TalkBack enabled
- Ensure items have proper content descriptions

## Code Example

```kotlin
LazyColumn(
    modifier = Modifier.semantics {
        collectionInfo = CollectionInfo(items.size, 1)
    }
) {
    items(items, key = { it.id }) { item ->
        ListItem(
            modifier = Modifier.semantics {
                role = Role.Button
                stateDescription = "Item ${item.position}"
            }
        )
    }
}
```

# collectionInfo: define scrollable collection
# role: item type for accessibility
# stateDescription: current item state
# Test with TalkBack
