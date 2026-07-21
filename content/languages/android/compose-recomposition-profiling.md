---
title: "Compose Recomposition Profiling"
description: "Profile and fix Jetpack Compose recomposition performance issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose UI shows jank because of excessive recomposition

## Common Causes

- Unstable types causing unnecessary recomposition
- Large composable trees recomposing entirely
- State changes propagating too broadly
- Remember not preventing recomposition of expensive computations

## Fixes

- Use Layout Inspector recompose counter to identify hotspots
- Mark data classes as @Stable or @Immutable
- Break large composables into smaller ones
- Use derivedStateOf for derived values

## Code Example

```kotlin
// Use stable types for parameters
@Stable
data class UiState(
    val items: List<Item>,
    val isLoading: Boolean
)

// Use remember for expensive computations
val processedItems = remember(items) {
    items.map { transformExpensive(it) }
}

// Use derivedStateOf for derived state
val visibleItems by remember {
    derivedStateOf { items.filter { it.visible } }
}
```

# Profile with Layout Inspector
# Recompose counter in developer options
# Use @Stable/@Immutable for data classes
