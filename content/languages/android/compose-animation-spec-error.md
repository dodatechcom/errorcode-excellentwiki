---
title: "Animation Spec Error"
description: "Fix Compose animation specification and timing errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Animation specs produce wrong timing, easing, or behavior

## Common Causes

- tween duration too short to see animation
- spring damping ratio causing overshoot
- keyframes not properly configured
- infiniteRepeatable not actually repeating

## Fixes

- Use appropriate duration (300-500ms typical)
- Adjust damping ratio for desired spring feel
- Set proper timestamps in keyframes
- Verify infiniteRepeatable has proper repeat mode

## Code Example

```kotlin
// Tween animation
val offsetY by animateDpAsState(
    targetValue = if (expanded) 200.dp else 0.dp,
    animationSpec = tween(
        durationMillis = 300,
        delayMillis = 50,
        easing = FastOutSlowInEasing
    )
)

// Spring animation
val scale by animateFloatAsState(
    targetValue = if (pressed) 1.2f else 1f,
    animationSpec = spring(
        dampingRatio = Spring.DampingRatioMediumBouncy,
        stiffness = Spring.StiffnessLow
    )
)

// Keyframes animation
val value by animateFloatAsState(
    targetValue = targetValue,
    animationSpec = keyframes {
        durationMillis = 1000
        0f at 0 with LinearEasing
        0.5f at 300
        1f at 600 with FastOutSlowInEasing
    }
)
```

# tween: duration + easing
# spring: damping + stiffness
# keyframes: value at specific times
# infiniteRepeatable: repeat forever
