---
title: "Compose Drag Drop Error"
description: "Fix Compose drag and drop gesture and modifier errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Drag and drop does not work or items do not reorder correctly

## Common Causes

- detectDragGestures not responding
- Drag offset not properly calculated
- Items not visually updating during drag
- Drop target not detecting drag enter/exit

## Fixes

- Use Modifier.pointerInput with detectDragGestures
- Track drag offset with MutableState
- Update list order during drag
- Use onDragStarted and onDragStopped callbacks

## Code Example

```kotlin
var items by remember { mutableStateOf(listOf("A", "B", "C")) }

LazyColumn {
    itemsIndexed(items, key = { _, item -> item }) { index, item ->
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .pointerInput(item) {
                    detectDragGestures(
                        onDragStart = { /* start drag */ },
                        onDrag = { change, dragAmount ->
                            change.consume()
                            // Reorder items based on drag
                        },
                        onDragEnd = { /* finish drag */ }
                    )
                }
        ) {
            Text(item)
        }
    }
}
```

# detectDragGestures: basic drag
# detectDragGesturesAfterLongPress: drag after long press
# Track offset with mutableStateOf
