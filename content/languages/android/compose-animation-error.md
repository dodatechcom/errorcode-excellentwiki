---
title: "Compose Animation Error"
description: "Fix Jetpack Compose animation errors with animateContentSize and transitions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose animations fail to run or produce visual glitches

## Common Causes

- animateContentSize not triggering on state change
- Transition not properly defined with updateTransition
- InfiniteTransition missing target value
- AnimationSpec not compatible with property type

## Fixes

- Ensure state change actually occurs for animateContentSize
- Define fromState and toState in Transition
- Use rememberInfiniteTransition with animateFloat
- Use appropriate AnimationSpec for animation type

## Code Example

```kotlin
// animateContentSize
var expanded by remember { mutableStateOf(false) }
Box(modifier = Modifier.animateContentSize()) {
    if (expanded) {
        ExpandedContent()
    } else {
        CollapsedContent()
    }
}

// Infinite animation
val infiniteTransition = rememberInfiniteTransition()
val alpha by infiniteTransition.animateFloat(
    initialValue = 0f,
    targetValue = 1f,
    animationSpec = infiniteRepeatable(
        animation = tween(1000),
        repeatMode = RepeatMode.Reverse
    )
)
```

# Use animateXAsState for simple animations
# Use AnimatedVisibility for appear/disappear
# Use Crossfade for content swaps
