---
title: "LazyRow Scroll Error"
description: "Fix LazyRow horizontal scrolling and item arrangement errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyRow does not scroll horizontally or items not properly arranged

## Common Causes

- LazyRow scrolling vertically instead
- Items not fitting in viewport
- Horizontal arrangement not working
- Edge spacing incorrect

## Fixes

- Use LazyRow for horizontal scrolling
- Set horizontalArrangement for spacing
- Use contentPadding for edge spacing
- Test on different screen widths

## Code Example

```kotlin
LazyRow(
    modifier = Modifier.fillMaxWidth(),
    contentPadding = PaddingValues(horizontal = 16.dp),
    horizontalArrangement = Arrangement.spacedBy(8.dp)
) {
    items(items, key = { it.id }) { item ->
        Card(modifier = Modifier.width(200.dp)) {
            ListItem(item)
        }
    }
}
```

# LazyRow: horizontal scrolling
# horizontalArrangement: spacing between items
# contentPadding: edge spacing
# Fixed width items for consistent sizing
