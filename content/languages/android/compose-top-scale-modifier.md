---
title: "Scale Modifier Error"
description: "Fix Compose scale modifier for scaling transformations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable scaling not applying correctly or causing rendering issues

## Common Causes

- Scale not resizing composable
- Scale affecting parent layout
- Scale origin not matching expected pivot
- Scale causing text rendering issues

## Fixes

- Use graphicsLayer for scaling
- Use scale modifier for simple scaling
- Ensure scale does not affect layout
- Test scale with different content types

## Code Example

```kotlin
Modifier.graphicsLayer(
    scaleX = 1.5f,
    scaleY = 1.5f,
    transformOrigin = TransformOrigin(0.5f, 0.5f)
)

// Simple scale:
Modifier.scale(1.5f)
```

# graphicsLayer: scale with pivot# scale(): simple scaling# transformOrigin: pivot point# Does not affect parent layout
