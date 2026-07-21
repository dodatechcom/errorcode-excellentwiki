---
title: "Infinite Transition Error"
description: "Fix infinite transition animation errors in Jetpack Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Infinite animation does not play or stops unexpectedly

## Common Causes

- rememberInfiniteTransition not called in composition
- animateFloat not returning correct AnimatedValue
- RepeatMode not producing expected behavior
- Animation spec causing stack overflow

## Fixes

- Call rememberInfiniteTransition() in composition
- Use value.value to get current animated value
- Use RepeatMode.Reverse or RepeatMode.Restart
- Ensure animation values stay within range

## Code Example

```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "pulse")

val scale by infiniteTransition.animateFloat(
    initialValue = 0.8f,
    targetValue = 1.2f,
    animationSpec = infiniteRepeatable(
        animation = tween(1000, easing = LinearEasing),
        repeatMode = RepeatMode.Reverse
    ),
    label = "scale"
)

Box(
    Modifier.graphicsLayer {
        scaleX = scale
        scaleY = scale
    }
) {
    Text("Pulsing")
}
```

# rememberInfiniteTransition: remember across recompositions
# infiniteRepeatable: repeat forever
# tween, keyframes, repeatable for different effects
