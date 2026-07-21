---
title: "Flow Layout Error"
description: "Fix Compose FlowRow and FlowColumn layout wrapping errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
FlowRow or FlowColumn does not wrap items correctly

## Common Causes

- Items not wrapping to next line
- Spacing between items incorrect
- Flow layout not available in older Compose
- Cross-axis spacing not working

## Fixes

- Use FlowRow from Accompanist or Compose 1.4+
- Set horizontalArrangement and verticalArrangement
- Provide item spacing with Arrangement.spacedBy
- Use maxItemsInEachRow for column limit

## Code Example

```kotlin
// Compose Foundation FlowRow
FlowRow(
    horizontalArrangement = Arrangement.spacedBy(8.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp),
    maxItemsInEachRow = 3
) {
    items.forEach { item ->
        Chip(text = item.name)
    }
}
```

# FlowRow: wraps horizontally then vertically
# FlowColumn: wraps vertically then horizontally
# Arrangement.spacedBy: item spacing
# maxItemsInEachRow: limit columns
