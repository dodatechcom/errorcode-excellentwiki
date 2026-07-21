---
title: "GraphicsLayer Error"
description: "Fix Compose graphicsLayer modifier and rendering effects errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
GraphicsLayer modifier produces incorrect visual effects or performance issues

## Common Causes

- graphicsLayer not applied to correct modifier
- Rendering effect not visible because of wrong order
- graphicsLayer causing unnecessary recomposition
- Alpha or rotation not animating smoothly

## Fixes

- Apply graphicsLayer before clickable modifier
- Use graphicsLayer for transform effects
- Cache graphicsLayer calculations with remember
- Use animateFloatAsState for smooth animations

## Code Example

```kotlin
Box(
    modifier = Modifier
        .graphicsLayer {
            rotationZ = rotationAngle
            alpha = if (isVisible) 1f else 0f
            scaleX = scale
            scaleY = scale
            shadowElevation = elevation
        }
        .clickable { onClick() }
)
```

# graphicsLayer: transform and visual effects
# rotationZ/X/Y: rotation in degrees
# scaleX/Y: scaling factors
# alpha: transparency
# shadowElevation: drop shadow
