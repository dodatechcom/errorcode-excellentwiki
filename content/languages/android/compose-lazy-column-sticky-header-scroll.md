---
title: "Sticky Header Scroll Error"
description: "Fix LazyColumn sticky header scroll behavior and overlap errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Sticky headers overlap or do not stick correctly during scroll

## Common Causes

- Sticky header overlapping list items
- Header not sticking to top during scroll
- Multiple headers conflicting
- Header height affecting list padding

## Fixes

- Use stickyHeader with proper key
- Adjust header height for correct sticking
- Use one stickyHeader per section
- Test scroll behavior with multiple sections

## Code Example

```kotlin
LazyColumn {
    items.forEach { (section, sectionItems) ->
        stickyHeader(key = "header_$section") {
            Text(
                text = section,
                modifier = Modifier
                    .fillMaxWidth()
                    .background(MaterialTheme.colorScheme.surface)
                    .padding(horizontal = 16.dp, vertical = 8.dp),
                style = MaterialTheme.typography.titleMedium
            )
        }
        items(sectionItems, key = { it.id }) { item ->
            ItemRow(item)
        }
    }
}
```

# stickyHeader: sticks to top during scroll
# key: stable identity for headers
# Background on header prevents transparency
# One stickyHeader per section
