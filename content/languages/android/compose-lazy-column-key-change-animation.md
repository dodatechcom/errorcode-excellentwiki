---
title: "Key Change Animation Error"
description: "Fix LazyColumn animation issues when item keys change during update"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn shows wrong animations when item keys change during data update

## Common Causes

- Items animating incorrectly on key change
- Animation playing on all items instead of changed ones
- Remove animation not triggered for removed items
- Key change causing full list recomposition

## Fixes

- Ensure keys are stable and meaningful
- Use DiffUtil-style updates with stable keys
- Test with various data update patterns
- Verify animations only play for changed items

## Code Example

```kotlin
// Items with stable keys
items(items, key = { it.databaseId }) { item ->
    AnimatedContent(targetState = item) { currentItem ->
        ItemRow(currentItem)
    }
}
```

# databaseId as stable key# DiffUtil-style updates# Test add/remove/reorder animations# Verify animation targets
