---
title: "Scroll Indicator Error"
description: "Fix LazyColumn scroll indicator and scroll progress display"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn scroll indicator not showing or not tracking scroll position correctly

## Common Causes

- Scrollbar not appearing
- Scroll position not updating
- Indicator position inaccurate
- Custom scroll indicator not working

## Fixes

- Use scrollbar modifier for native indicator
- Track scrollState for custom indicator
- Calculate progress from firstVisibleItemIndex
- Animate indicator appearance

## Code Example

```kotlin
val listState = rememberLazyListState()
val scrollProgress by remember {
    derivedStateOf {
        if (listState.layoutInfo.totalItemsCount == 0) 0f
        else listState.firstVisibleItemIndex.toFloat() / listState.layoutInfo.totalItemsCount
    }
}

Box(modifier = Modifier.fillMaxSize()) {
    LazyColumn(state = listState) { items(items) { ItemRow(it) } }
    LinearProgressIndicator(progress = scrollProgress)
}
```

# scrollbar modifier for native indicator# derivedStateOf for scroll progress# Custom indicator with progress calculation# Animate indicator appearance
