---
title: "SubcomposeLayout Error"
description: "Fix Compose SubcomposeLayout and dynamic content measurement errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
SubcomposeLayout does not measure or place children correctly

## Common Causes

- SubcomposeLayout not measuring children in order
- Dynamic content causing infinite measurement
- Child measurement not respecting constraints
- Subcomposition not updating when data changes

## Fixes

- Use SubcomposeLayout for dynamic content
- Ensure finite number of children
- Measure children with appropriate constraints
- Cache subcomposition results

## Code Example

```kotlin
SubcomposeLayout { constraints ->
    val content = @Composable { Text("Dynamic") }
    val placeables = subcompose(0, content).map {
        it.measure(constraints)
    }
    val width = placeables.maxOfOrNull { it.width } ?: 0
    val height = placeables.sumOf { it.height }
    layout(width, height) {
        var y = 0
        placeables.forEach { placeable ->
            placeable.placeRelative(0, y)
            y += placeable.height
        }
    }
}
```

# SubcomposeLayout: compose during layout
# subcompose(slot, content): compose dynamic content
# Use sparingly - expensive operation
# Cache results when possible
