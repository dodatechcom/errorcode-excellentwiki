---
title: "AnimateAsState Error"
description: "Fix animateXAsState transition value errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
animateXAsState does not produce smooth transitions or correct values

## Common Causes

- AnimationSpec not appropriate for value type
- Target value not actually changing
- Animation not triggered on recomposition
- Multiple animateAsState calls conflicting

## Fixes

- Use appropriate animateXAsState for value type
- Ensure targetValue actually changes
- Use LaunchedEffect to trigger changes
- Chain animations with AnimationSpec

## Code Example

```kotlin
val size by animateDpAsState(
    targetValue = if (expanded) 200.dp else 100.dp,
    animationSpec = spring(
        dampingRatio = Spring.DampingRatioMediumBouncy,
        stiffness = Spring.StiffnessLow
    ),
    label = "size"
)

val color by animateColorAsState(
    targetValue = if (isSelected) Color.Red else Color.Gray,
    animationSpec = tween(durationMillis = 300),
    label = "color"
)

Box(
    Modifier
        .size(size)
        .background(color)
)
```

# animateDpAsState: dimension changes
# animateColorAsState: color transitions
# animateFloatAsState: float value changes
# animateIntAsState: integer changes
