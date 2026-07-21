---
title: "Rotate Modifier Error"
description: "Fix Compose rotate modifier for rotation transformations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable rotation not applying correctly or causing layout issues

## Common Causes

- Rotation not rotating composable
- Rotation affecting parent layout
- Rotation origin not matching expected pivot
- Rotation causing rendering artifacts

## Fixes

- Use rotate modifier with degrees
- Use graphicsLayer for rotation with pivot
- Ensure rotation does not affect layout
- Test rotation with different content types

## Code Example

```kotlin
Modifier.rotate(45f)  // Rotate 45 degrees

// Rotation with graphicsLayer:
Modifier.graphicsLayer(
    rotationZ = 45f,
    transformOrigin = TransformOrigin(0.5f, 0.5f)  // Center pivot
)
```

# rotate(): simple rotation# graphicsLayer: rotation with pivot# transformOrigin: pivot point# Does not affect parent layout
