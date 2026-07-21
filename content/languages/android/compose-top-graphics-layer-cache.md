---
title: "GraphicsLayer Cache Error"
description: "Fix Compose GraphicsLayer caching to prevent rendering artifacts"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
GraphicsLayer not correctly caching or invalidating composable rendering

## Common Causes

- Cached graphics showing stale content
- GraphicsLayer not updating after data change
- Rendering artifacts from cached layer
- Invalidation not triggering re-render

## Fixes

- Use GraphicsLayer with remember to cache correctly
- Invalidate graphics layer when content changes
- Avoid over-using graphicsLayer caching
- Test cached rendering across state changes

## Code Example

```kotlin
val graphicsLayer = rememberGraphicsLayer()
val canvas = rememberDrawScope()

Canvas(modifier = Modifier.fillMaxSize()) {
    drawLayer(graphicsLayer)
}

// Invalidate when content changes:
LaunchedEffect(newData) {
    graphicsLayer.record {
        drawContent()
    }
}
```

# GraphicsLayer: cache composable rendering# record {} to cache content# Invalidate on data change# Avoid over-caching
