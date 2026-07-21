---
title: "Complex Infinite Animation Error"
description: "Fix complex infinite animation patterns with multiple animated values in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Multiple infinite animations conflict or produce unexpected visual results

## Common Causes

- Multiple rememberInfiniteTransition calls conflicting
- Animation values not properly independent
- Combined animations causing jitter
- Animation timing not synchronized

## Fixes

- Use single infiniteTransition for related animations
- Ensure animations have independent target values
- Synchronize animations with same duration
- Profile animation performance with Compose metrics

## Code Example

```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "complex")

// Independent animations on same transition
val rotation by infiniteTransition.animateFloat(
    initialValue = 0f,
    targetValue = 360f,
    animationSpec = infiniteRepeatable(
        animation = tween(2000, easing = LinearEasing),
        repeatMode = RepeatMode.Restart
    ),
    label = "rotation"
)

val scale by infiniteTransition.animateFloat(
    initialValue = 0.8f,
    targetValue = 1.2f,
    animationSpec = infiniteRepeatable(
        animation = tween(1000),
        repeatMode = RepeatMode.Reverse
    ),
    label = "scale"
)

Box(
    Modifier.graphicsLayer {
        rotationZ = rotation
        scaleX = scale
        scaleY = scale
    }
)
```

# Single infiniteTransition for related animations
# Independent animateFloat calls for different effects
# Same or related durations for synchronized animations
