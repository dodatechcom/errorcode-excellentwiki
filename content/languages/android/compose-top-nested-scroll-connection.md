---
title: "Nested Scroll Connection Error"
description: "Fix Compose nestedScroll connection for coordinating multiple scrollable areas"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Multiple scrollable composables not coordinating scroll gestures correctly

## Common Causes

- Top scrollable area consuming all scroll events
- Bottom scrollable area not receiving scroll
- Nested scroll direction reversed
- Scroll fling not propagating correctly

## Fixes

- Implement NestedScrollConnection
- Dispatch and consume scroll correctly
- Handle preScroll, postScroll, and fling
- Test with AppBar + LazyColumn pattern

## Code Example

```kotlin
val connection = rememberNestedScrollConnection()

Box(modifier = Modifier.nestedScroll(connection)) {
    Column {
        TopAppBar(modifier = Modifier.offset { IntOffset(0, -scrollOffset) })
        LazyColumn { items(items) { ItemRow(it) } }
    }
}
```

# NestedScrollConnection: coordinate scrollables# preScroll: before child scrolls# postScroll: after child scrolls# Test with AppBar collapse pattern
