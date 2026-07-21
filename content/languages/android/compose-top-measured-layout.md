---
title: "MeasuredLayout Error"
description: "Fix Compose MeasuredLayout for custom measurement-based layouts"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom layout with MeasuredLayout not placing children correctly

## Common Causes

- Children not measured before placement
- Measurement order causing incorrect sizes
- Custom layout not respecting constraints
- Children overlapping or misplaced

## Fixes

- Measure children before placing
- Respect constraints from parent
- Use Placeable.place() or placeRelative() for placement
- Test with various child sizes

## Code Example

```kotlin
Layout(
    modifier = modifier,
    measurePolicy = { measurables, constraints ->
        val placeables = measurables.map { measurable ->
            measurable.measure(constraints)
        }
        
        val totalWidth = placeables.maxOfOrNull { it.width } ?: 0
        val totalHeight = placeables.sumOf { it.height }
        
        layout(totalWidth, totalHeight) {
            var y = 0
            placeables.forEach { placeable ->
                placeable.placeRelative(0, y)
                y += placeable.height
            }
        }
    }
)
```

# Layout: custom measurement policy# measure(): measure child with constraints# Placeable.place(): place at position# Respect parent constraints
