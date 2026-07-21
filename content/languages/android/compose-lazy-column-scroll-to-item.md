---
title: "LazyColumn Scroll Error"
description: "Fix LazyColumn scroll to item and programmatic scrolling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn does not scroll to specific item programmatically

## Common Causes

- scrollToItem not working correctly
- animateScrollToItem not smooth
- Scroll position not preserved after scroll
- Scroll to item not working in nested lists

## Fixes

- Use scrollToItem for instant scroll
- Use animateScrollToItem for smooth scroll
- Save scroll position with rememberLazyListState
- Handle nested scroll with nestedScroll modifier

## Code Example

```kotlin
val listState = rememberLazyListState()

// Programmatic scroll:
Button(onClick = {
    coroutineScope.launch {
        listState.animateScrollToItem(index = 10)
    }
}) {
    Text("Scroll to item 10")
}

// Or instant scroll:
listState.scrollToItem(index = 0)

// LazyColumn with state:
LazyColumn(state = listState) {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}
```

# scrollToItem: instant scroll
# animateScrollToItem: smooth scroll
# rememberLazyListState: track and control scroll
# Launch in coroutineScope
