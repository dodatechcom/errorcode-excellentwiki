---
title: "LazyGrid Configuration Error"
description: "Fix LazyVerticalGrid configuration and span errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyVerticalGrid does not display items in correct grid layout

## Common Causes

- GridCells not properly configured
- Item span not matching expected layout
- Grid not scrolling correctly
- Content padding causing alignment issues

## Fixes

- Use GridCells.Fixed or GridCells.Adaptive
- Set span with item span parameter
- Use contentPadding for grid margins
- Configure horizontalArrangement for spacing

## Code Example

```kotlin
LazyVerticalGrid(
    columns = GridCells.Fixed(2),  // 2 columns
    contentPadding = PaddingValues(16.dp),
    horizontalArrangement = Arrangement.spacedBy(8.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp)
) {
    items(items, key = { it.id }) { item ->
        GridItem(item)
    }
}

// Adaptive columns based on width:
LazyVerticalGrid(
    columns = GridCells.Adaptive(minSize = 128.dp),
    ...
)
```

# GridCells.Fixed(n): fixed column count
# GridCells.Adaptive(minSize): responsive columns
# Spacing with Arrangement.spacedBy()
