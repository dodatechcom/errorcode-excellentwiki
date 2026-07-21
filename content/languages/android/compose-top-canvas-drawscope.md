---
title: "Canvas DrawScope Error"
description: "Fix Compose Canvas DrawScope for custom drawing and rendering"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom Canvas drawing not rendering correctly or causing performance issues

## Common Causes

- Drawing not visible on screen
- Canvas not filling available space
- Drawing commands not executed in correct order
- Performance issues with complex Canvas

## Fixes

- Use DrawScope for custom drawing commands
- Ensure Canvas fills available space
- Use offset and translation for positioning
- Cache complex drawings with GraphicsLayer

## Code Example

```kotlin
Canvas(
    modifier = Modifier
        .fillMaxSize()
        .background(Color.White)
) {
    drawLine(
        color = Color.Red,
        start = Offset(0f, 0f),
        end = Offset(size.width, size.height),
        strokeWidth = 5f
    )
    
    drawCircle(
        color = Color.Blue,
        radius = 50f,
        center = Offset(size.width / 2, size.height / 2)
    )
}
```

# DrawScope: custom drawing commands# drawLine/drawCircle/drawRect# offset for positioning# GraphicsLayer for complex drawings
