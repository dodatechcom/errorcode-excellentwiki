---
title: "LazyColumn Sticky Header Error"
description: "Fix LazyColumn sticky header and section header errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Sticky headers do not stick or overlap with list content

## Common Causes

- stickyHeader not placed before items
- Header content not matching section
- Header overlapping list items
- Multiple headers conflicting

## Fixes

- Place stickyHeader before related items block
- Use key parameter for stable headers
- Adjust contentPadding for header height
- Use one stickyHeader per section

## Code Example

```kotlin
LazyColumn {
    items.forEach { (section, items) ->
        stickyHeader(key = section) {
            Text(
                text = section,
                modifier = Modifier
                    .fillMaxWidth()
                    .background(MaterialTheme.colorScheme.surface)
                    .padding(16.dp)
            )
        }
        items(items, key = { it.id }) { item ->
            ListItem(item)
        }
    }
}
```

# stickyHeader before items for each section
# Use key for stable header identity
# Headers stack when scrolled
