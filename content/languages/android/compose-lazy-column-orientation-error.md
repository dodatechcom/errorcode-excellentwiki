---
title: "LazyColumn Orientation Error"
description: "Fix LazyColumn horizontal scrolling and orientation configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn scrolls in wrong direction or horizontal scroll not working

## Common Causes

- LazyColumn scrolling horizontally instead of vertically
- LazyRow not scrolling horizontally
- Orientation not properly configured
- Nested scroll lists conflicting

## Fixes

- Use LazyColumn for vertical scrolling
- Use LazyRow for horizontal scrolling
- Check orientation parameter
- Handle nested scroll properly

## Code Example

```kotlin
// Vertical list (default)
LazyColumn {
    items(items) { item ->
        ItemRow(item)
    }
}

// Horizontal list
LazyRow(
    modifier = Modifier.fillMaxWidth(),
    horizontalArrangement = Arrangement.spacedBy(8.dp)
) {
    items(items) { item ->
        HorizontalItem(item)
    }
}

// Grid layout
LazyVerticalGrid(
    columns = GridCells.Fixed(2)
) {
    items(items) { item ->
        GridItem(item)
    }
}
```

# LazyColumn: vertical scrolling
# LazyRow: horizontal scrolling
# LazyVerticalGrid: grid layout
# LazyHorizontalGrid: horizontal grid
