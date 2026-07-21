---
title: "Drag Reorder Error"
description: "Fix LazyColumn drag-and-drop reorder implementation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items cannot be reordered by drag and drop

## Common Causes

- Drag gesture not detected on items
- Item position not updating during drag
- Drag overlay not showing correctly
- Reorder callback not firing

## Fixes

- Use detectDragGesturesAfterLongPress for drag detection
- Track dragged item index and swap on drop
- Show drag overlay with item content
- Update list in ViewModel on reorder complete

## Code Example

```kotlin
val lazyListState = rememberLazyListState()
var draggedIndex by remember { mutableStateOf<Int?>(null) }

LazyColumn(state = lazyListState) {
    items(items, key = { it.id }) { item ->
        Row(
            modifier = Modifier.pointerInput(item.id) {
                detectDragGesturesAfterLongPress(
                    onDragStart = { draggedIndex = items.indexOf(item) },
                    onDrag = { change, dragAmount -> change.consume() },
                    onDragEnd = { draggedIndex = null }
                )
            }
        ) { ItemRow(item) }
    }
}
```

# detectDragGesturesAfterLongPress: initiate drag# Track dragged item index# Swap items on drop# Update list state
