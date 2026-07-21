---
title: "LazyGrid Span Error"
description: "Fix LazyVerticalGrid item span and column configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyVerticalGrid items do not span correct number of columns

## Common Causes

- Item span not matching expected width
- Grid items not filling available space
- Span configuration not working
- Grid not responsive to screen size

## Fixes

- Use span parameter for item column span
- Set GridCells.Fixed or GridCells.Adaptive
- Test on different screen sizes
- Use fillMaxWidth for full-width items

## Code Example

```kotlin
LazyVerticalGrid(
    columns = GridCells.Fixed(3),
    modifier = Modifier.fillMaxWidth()
) {
    items(items, key = { it.id }) { item ->
        GridItem(item)
    }
}

// Span specific item across columns:
LazyVerticalGrid(
    columns = GridCells.Fixed(3)
) {
    item(span = { GridItemSpan(3) }) {
        FullWidthItem()  // Spans all 3 columns
    }
    items(items) { item ->
        GridItem(item)  // Takes 1 column
    }
}
```

# GridCells.Fixed(n): fixed columns
# GridCells.Adaptive: responsive columns
# GridItemSpan(n): span n columns
# item(span) for specific item span
