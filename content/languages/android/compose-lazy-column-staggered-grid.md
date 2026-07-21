---
title: "Staggered Grid Error"
description: "Fix LazyVerticalStaggeredGrid layout and column spanning errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyVerticalStaggeredGrid items not arranged correctly across staggered columns

## Common Causes

- Items not spanning correct columns
- Grid columns not matching expected layout
- Staggered layout not responsive
- Items overlapping in grid

## Fixes

- Configure StaggeredGridCells for columns
- Use span property for full-width items
- Test with different screen sizes
- Set proper item spacing

## Code Example

```kotlin
LazyVerticalStaggeredGrid(
    columns = StaggeredGridCells.Fixed(3),
    modifier = Modifier.fillMaxSize()
) {
    items(items, key = { it.id }) { item ->
        StaggeredGridItem(item)
    }
}
```

# StaggeredGridCells.Fixed/Adaptive: column count# span for specific item column span# Test on various screen sizes# Use fixed heights for consistent layout
