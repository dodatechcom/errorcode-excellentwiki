---
title: "Responsive Grid Error"
description: "Fix LazyVerticalGrid responsive column count based on screen width"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyVerticalGrid columns not adapting to different screen sizes

## Common Causes

- Grid showing wrong number of columns on different screens
- Columns too wide on tablets
- Columns too narrow on phones
- Grid not responsive to orientation changes

## Fixes

- Use GridCells.Adaptive for responsive columns
- Test on phone, tablet, and foldable
- Use WindowSizeClass for breakpoints
- Handle orientation changes with different column counts

## Code Example

```kotlin
LazyVerticalGrid(
    columns = GridCells.Adaptive(minSize = 128.dp)
) {
    items(items, key = { it.id }) { item ->
        GridItem(item)
    }
}

// Or with WindowSizeClass:
val columns = when (windowSizeClass.widthSizeClass) {
    WindowWidthSizeClass.Compact -> GridCells.Fixed(2)
    WindowWidthSizeClass.Medium -> GridCells.Fixed(3)
    WindowWidthSizeClass.Expanded -> GridCells.Fixed(4)
    else -> GridCells.Fixed(2)
}
```

# GridCells.Adaptive: responsive based on min size# WindowSizeClass: breakpoint-based columns# Test on various screen sizes# Handle orientation changes
