---
title: "Layout Modifier Error"
description: "Fix Compose Layout modifier for measuring and placing composable content"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Layout modifier not measuring or placing content correctly in custom layouts

## Common Causes

- Content not measured with correct constraints
- Placement not respecting measured size
- Layout modifier causing measurement cycle
- Content overflowing layout bounds

## Fixes

- Use layout modifier for custom measurement
- Measure content with incoming constraints
- Place content at correct positions
- Test with different content sizes

## Code Example

```kotlin
Modifier.layout { measurable, constraints ->
    val placeable = measurable.measure(constraints)
    layout(placeable.width, placeable.height) {
        placeable.placeRelative(0, 0)
    }
}

// With custom sizing:
Modifier.layout { measurable, constraints ->
    val placeable = measurable.measure(
        constraints.copy(minWidth = 100, maxWidth = 200)
    )
    layout(200, placeable.height) {
        placeable.placeRelative(0, 0)
    }
}
```

# layout modifier: custom measurement# measurable.measure(): measure content# constraints: incoming size constraints# placeable.place(): position content
