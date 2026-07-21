---
title: "LazyColumn Header Footer Error"
description: "Fix LazyColumn header and footer placement with item blocks"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Header and footer not properly positioned or styled in LazyColumn

## Common Causes

- Header not staying at top
- Footer overlapping list content
- Header and footer not full width
- Spacing between header and list incorrect

## Fixes

- Use item { } block for header and footer
- Place header before items and footer after
- Set full width on header/footer content
- Use proper spacing between sections

## Code Example

```kotlin
LazyColumn {
    // Header
    item {
        Text(
            "Section Title",
            modifier = Modifier.fillMaxWidth().padding(16.dp),
            style = MaterialTheme.typography.headlineMedium
        )
    }

    // List items
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }

    // Footer
    item {
        Text(
            "End of list",
            modifier = Modifier.fillMaxWidth().padding(16.dp),
            textAlign = TextAlign.Center
        )
    }
}
```

# item { } for single items (header/footer)
# items() for list items
# Place header before items
# Place footer after items
