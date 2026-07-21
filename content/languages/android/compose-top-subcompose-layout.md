---
title: "SubcomposeLayout Error"
description: "Fix Compose SubcomposeLayout for dynamic content measurement and placement"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
SubcomposeLayout not measuring or placing sub-composables correctly

## Common Causes

- Sub-composables not appearing in layout
- Measurement cycle exceeding limit
- SubcomposeLayout causing infinite measurement
- Content slot not filling available space

## Fixes

- Use SubcomposeLayout for dynamic slot content
- Ensure sub-composables do not cause infinite measurement
- Measure sub-composables after main layout
- Test with varying sub-composable sizes

## Code Example

```kotlin
SubcomposeLayout { constraints ->
    val mainPlaceables = subcompose("main") { MainContent() }.map {
        it.measure(constraints)
    }
    
    val totalHeight = mainPlaceables.sumOf { it.height }
    
    layout(constraints.maxWidth, totalHeight) {
        var yPosition = 0
        mainPlaceables.forEach { placeable ->
            placeable.placeRelative(0, yPosition)
            yPosition += placeable.height
        }
    }
}
```

# SubcomposeLayout: dynamic content slots# subcompose("key") for slot content# Measure after main layout# Avoid infinite measurement cycles
