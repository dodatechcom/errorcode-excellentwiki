---
title: "Compose Scroll Accessibility Error"
description: "Fix Compose LazyColumn scroll accessibility for screen readers"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items not accessible or scroll actions not working with TalkBack

## Common Causes

- LazyColumn items not announced by screen reader
- Scroll actions not triggered by accessibility gesture
- Item type information not provided
- Collection semantics not defined

## Fixes

- Use semantics properties for LazyColumn
- Provide collection info in semantics
- Test with TalkBack enabled
- Use semantics merge for grouped content

## Code Example

```kotlin
LazyColumn(
    modifier = Modifier.semantics {
        collectionInfo = CollectionInfo(itemCount, columnCount)
    }
) {
    items(items, key = { it.id }) { item ->
        ListItem(
            modifier = Modifier.semantics {
                role = Role.Button
                stateDescription = "Item ${item.position} of ${items.size}"
            }
        )
    }
}
```

# collectionInfo: defines scrollable collection
# role: button, tab, checkbox, etc.
# stateDescription: current state announcement
# Test with TalkBack
