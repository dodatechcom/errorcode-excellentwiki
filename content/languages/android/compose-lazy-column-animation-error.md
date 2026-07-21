---
title: "LazyColumn Animation Error"
description: "Fix LazyColumn item animation and placement errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items do not animate correctly when reordered or removed

## Common Causes

- Item animation not playing on reorder
- Remove animation not smooth
- Items jumping instead of animating
- Animation spec not configured for LazyColumn

## Fixes

- Use Modifier.animateItemPlacement for reordering
- Configure animation spec for smooth transitions
- Use key for stable item identity
- Test animations with different list operations

## Code Example

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .animateItemPlacement(
                    animationSpec = tween(durationMillis = 300)
                )
        ) {
            ItemRow(item)
        }
    }
}
```

# animateItemPlacement: animate on reorder
# animationSpec: configure animation timing
# key: stable identity for animations
# Test with add/remove/reorder operations
