---
title: "LazyColumn Content Padding Error"
description: "Fix LazyColumn content padding and edge spacing for scrollable content"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn content not properly padded from edges causing overlap with system UI

## Common Causes

- Content overlapping system bars
- Edge padding not applied correctly
- Bottom padding cut off by navigation bar
- Content not respecting inset padding

## Fixes

- Use contentPadding for LazyColumn edges
- Apply WindowInsets padding for system UI
- Test on devices with notch/cutout
- Use safe drawing insets

## Code Example

```kotlin
LazyColumn(
    contentPadding = PaddingValues(
        top = WindowInsets.statusBars.asPaddingValues().calculateTopPadding(),
        bottom = WindowInsets.navigationBars.asPaddingValues().calculateBottomPadding()
    )
) {
    items(items) { ItemRow(it) }
}
```

# contentPadding: edge spacing# WindowInsets: system UI padding# Test on various device types# safeDrawing insets for proper spacing
