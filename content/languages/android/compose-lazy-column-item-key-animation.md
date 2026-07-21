---
title: "LazyColumn Key Animation Error"
description: "Fix LazyColumn item key and animation interaction for smooth list updates"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn animations conflict with key-based identity causing visual glitches

## Common Causes

- Key changing during animation
- Animation playing on items without key changes
- Reorder animation not smooth with keys
- Remove animation not triggered

## Fixes

- Ensure keys are stable during animation
- Use animateItemPlacement for reorder animations
- Test with add/remove/reorder operations
- Verify animation timing with key changes

## Code Example

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .animateItemPlacement()
        ) {
            ItemRow(item)
        }
    }
}
```

# key: stable identity
# animateItemPlacement: smooth reorder
# Test all list operations
# Verify animation timing
