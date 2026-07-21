---
title: "GraphicsLayer Modifier Error"
description: "Fix Compose graphicsLayer modifier for hardware-accelerated transformations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
graphicsLayer not applying transformations correctly or causing performance issues

## Common Causes

- Transformation not applying to composable
- GraphicsLayer causing performance issues
- Transformation not matching expected result
- GraphicsLayer not invalidating correctly

## Fixes

- Use graphicsLayer for hardware-accelerated transformations
- Use rememberGraphicsLayer for caching
- Invalidate graphics layer when content changes
- Test with different transformation combinations

## Code Example

```kotlin
Modifier.graphicsLayer(
    scaleX = 1f,
    scaleY = 1f,
    rotationZ = 0f,
    translationX = 0f,
    translationY = 0f,
    transformOrigin = TransformOrigin(0.5f, 0.5f)
)
```

# graphicsLayer: hardware-accelerated transformations# rememberGraphicsLayer: cache transformations# Invalidate on content change# Test transformation combinations
