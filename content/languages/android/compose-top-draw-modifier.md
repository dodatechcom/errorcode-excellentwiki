---
title: "Draw Modifier Error"
description: "Fix Compose draw modifier for custom drawing behind or in front of content"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom drawing behind or in front of composable content not rendering correctly

## Common Causes

- Drawing not appearing behind content
- Drawing overlapping content incorrectly
- drawBehind not covering full area
- drawWithContent not drawing correctly

## Fixes

- Use drawBehind for drawing behind content
- Use drawWithContent for drawing with content
- Use drawWithCache for cached drawing
- Test drawing order and visibility

## Code Example

```kotlin
Modifier
    .drawBehind {
        drawRect(
            color = Color.Red.copy(alpha = 0.5f),
            size = size
        )
    }

// Drawing with content:
Modifier.drawWithContent {
    drawContent()
    drawCircle(
        color = Color.Blue,
        radius = 50f,
        center = Offset(size.width / 2, size.height / 2)
    )
}
```

# drawBehind: behind content# drawWithContent: with content# drawWithCache: cached drawing# Test drawing order
