---
title: "Pager Integration Error"
description: "Fix HorizontalPager and VerticalPager integration with LazyColumn"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
HorizontalPager or VerticalPager conflicts with LazyColumn scrolling

## Common Causes

- Pager intercepting LazyColumn scroll gestures
- Nested scrolling not coordinated
- Pager and LazyColumn scroll simultaneously
- HorizontalPager not responding to horizontal swipes

## Fixes

- Use nestedScroll to coordinate pager and list scrolling
- Disable pager scroll when list is scrolling
- Use PagerState for programmatic control
- Test swipe gestures between pager and list

## Code Example

```kotlin
val pagerState = rememberPagerState()
val listState = rememberLazyListState()

HorizontalPager(state = pagerState) { page ->
    LazyColumn(state = listState) {
        items(pagedItems[page]) { ItemRow(it) }
    }
}
```

# PagerState for pager control# LazyListState for list control# nestedScroll for gesture coordination# Test swipe and scroll interactions
