---
title: "Canvas Drawing Error"
description: "Fix Compose Canvas drawing and custom rendering errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom Canvas drawing does not render correctly or causes performance issues

## Common Causes

- Draw scope not properly sized
- Path operations causing rendering artifacts
- Canvas not redrawing on state changes
- Custom drawing consuming too much CPU

## Fixes

- Use drawWithContent for custom drawing
- Cache paths and paint objects
- Use Canvas with proper size constraints
- Optimize drawing operations for 60fps

## Code Example

```kotlin
Canvas(
    modifier = Modifier
        .fillMaxWidth()
        .height(200.dp)
) {
    // Draw rectangle
    drawRect(
        color = Color.Blue,
        topLeft = Offset(10f, 10f),
        size = Size(size.width - 20f, size.height - 20f),
        style = Stroke(width = 2.dp.toPx())
    )

    // Draw circle
    drawCircle(
        color = Color.Red,
        radius = 50.dp.toPx(),
        center = Offset(size.width / 2, size.height / 2)
    )

    // Draw line
    drawLine(
        color = Color.Green,
        start = Offset(0f, 0f),
        end = Offset(size.width, size.height),
        strokeWidth = 4.dp.toPx()
    )
}
```

# Canvas provides draw scope
# drawRect, drawCircle, drawLine, drawPath
# Use .dp.toPx() for density-independent drawing
