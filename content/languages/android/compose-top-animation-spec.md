---
title: "Animation Spec Error"
description: "Fix Compose animation specification for correct transition behavior"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose animations not behaving as expected because of incorrect animation spec

## Common Causes

- Animation too fast or too slow
- Spring animation not bouncing correctly
- Easing curve not matching expected behavior
- Repeat mode not working

## Fixes

- Use appropriate AnimationSpec type
- Tune spring parameters for desired feel
- Test animation specs with AnimationPreview
- Use tween, spring, or keyframes as needed

## Code Example

```kotlin
// Smooth transition
val offsetX by animateDpAsState(
    targetValue = if (expanded) 200.dp else 0.dp,
    animationSpec = spring(
        dampingRatio = Spring.DampingRatioMediumBouncy,
        stiffness = Spring.StiffnessLow
    )
)

// Keyframe animation
val progress by animateFloatAsState(
    targetValue = 1f,
    animationSpec = keyframes {
        durationMillis = 1000
        0f at 0
        0.5f at 500 with EaseIn
        1f at 1000 with EaseOut
    }
)
```

# spring(): physics-based animation# tween(): time-based with easing# keyframes(): custom keyframe points# Test specs with AnimationPreview
