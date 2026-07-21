---
title: "Compose Drag Drop List Error"
description: "Fix Compose LazyColumn drag and drop reordering implementation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items do not reorder correctly when dragged

## Common Causes

- Drag gesture not detected on list items
- Item positions not updating during drag
- Drop target not detecting valid drop zone
- Animation not smooth during reorder

## Fixes

- Use Modifier.pointerInput for drag detection
- Update list state on drag completion
- Animate item movement during drag
- Use key for stable item identity

## Code Example

```kotlin
var items by remember { mutableStateOf(listOf("A", "B", "C", "D")) }

LazyColumn {
    items(items, key = { it }) { item ->
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .pointerInput(item) {
                    detectDragGestures(
                        onDrag = { change, dragAmount ->
                            change.consume()
                            // Calculate new position and reorder
                        }
                    )
                }
                .dragAndDropTarget(
                    startTransaction = { /* start */ },
                    onDrop = { /* handle drop */ }
                )
        ) {
            Text(item, modifier = Modifier.padding(16.dp))
        }
    }
}
```

# Use key for stable item identity
# detectDragGestures for drag detection
# Update list state on drag completion
# Animate reorder with animateItemPlacement
