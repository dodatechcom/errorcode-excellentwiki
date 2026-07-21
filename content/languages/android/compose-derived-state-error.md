---
title: "DerivedStateOf Error"
description: "Fix Jetpack Compose derivedStateOf performance and correctness errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
derivedStateOf not triggering or producing stale values

## Common Causes

- derivedStateOf key not actually changing
- derivedStateOf used when snapshotFlow would be better
- Multiple state dependencies causing unexpected recomposition
- derivedStateOf not memoizing expensive computation

## Fixes

- Ensure source state actually changes
- Use derivedStateOf for state derived from other state
- Use snapshotFlow for side-effect based on state changes
- Profile to verify recomposition reduction

## Code Example

```kotlin
// CORRECT: derivedStateOf reduces recompositions
val scrollState = rememberLazyListState()

// Only recompose when isScrollingFirst actually changes
val showButton by remember {
    derivedStateOf { !scrollState.firstVisibleItemIndex == 0 }
}

// WRONG: recomposes on every scroll pixel change
val showButton = scrollState.firstVisibleItemIndex == 0

// snapshotFlow for side effects:
LaunchedEffect(scrollState) {
    snapshotFlow { scrollState.firstVisibleItemIndex }
        .collect { index -> analytics.logScroll(index) }
}
```

# derivedStateOf: reduces recomposition frequency
# snapshotFlow: converts Compose state to Flow
# Use for performance-critical state derivations
