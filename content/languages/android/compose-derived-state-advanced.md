---
title: "Advanced DerivedState Error"
description: "Fix advanced derivedStateOf patterns for complex state derivations in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Complex state derivations with derivedStateOf produce incorrect or stale values

## Common Causes

- Multiple state sources not properly combined
- derivedStateOf not memoizing expensive computation
- State derivation creating infinite recomposition loop
- derivedStateOf used when computed value should change every time

## Fixes

- Use derivedStateOf for stable state derivations
- Use snapshotFlow for event-based derivations
- Ensure source states actually change
- Profile to verify recomposition count is reduced

## Code Example

```kotlin
// Complex derivation
val scrollState = rememberLazyListState()

// Derive multiple states
val isAtTop by remember {
    derivedStateOf { scrollState.firstVisibleItemIndex == 0 }
}

val scrollPercentage by remember {
    derivedStateOf {
        val totalItems = scrollState.layoutInfo.totalItemsCount
        val visibleItems = scrollState.layoutInfo.visibleItemsInfo.size
        val scrolled = scrollState.firstVisibleItemIndex
        if (totalItems > 0) scrolled.toFloat() / totalItems else 0f
    }
}

// When to use derivedStateOf vs snapshotFlow:
// derivedStateOf: when you need a STATE value
// snapshotFlow: when you need a SIDE EFFECT
```

# derivedStateOf reduces recomposition
# snapshotFlow for side effects based on state
# Use when derivation is expensive
