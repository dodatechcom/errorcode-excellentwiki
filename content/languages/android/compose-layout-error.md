---
title: "Compose Layout Error"
description: "Fix Jetpack Compose layout measurement and positioning errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose custom layout does not measure or position children correctly

## Common Causes

- Custom Layout not calling measurables.measure()
- Placeable.place() coordinates incorrect
- Missing constraint on measured size
- Layout infinite constraint causes crash

## Fixes

- Call measurable.measure(constraints) for each child
- Use place(x, y) with correct coordinates
- Apply constraints.minWidth/Height before measuring
- Avoid placing content in infinite constraints

## Code Example

```kotlin
@Composable
fun MyCustomLayout(
    modifier: Modifier = Modifier,
    content: @Composable () -> Unit
) {
    Layout(
        modifier = modifier,
        content = content
    ) { measurables, constraints ->
        val placeables = measurables.map { measurable ->
            measurable.measure(constraints.copy(maxWidth = constraints.maxWidth / 2))
        }
        layout(
            width = constraints.maxWidth,
            height = placeables.sumOf { it.height }
        ) {
            var yPosition = 0
            placeables.forEach { placeable ->
                placeable.placeRelative(x = 0, y = yPosition)
                yPosition += placeable.height
            }
        }
    }
}
```

# Use BoxWithConstraints for responsive layouts
# Use Column/Row instead of custom Layout when possible
