---
title: "Complex Transition Error"
description: "Fix Compose complex transition and animation state machine errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Complex transition state machine produces unexpected animations

## Common Causes

- Transition not properly initialized with states
- animateColorAsState not responding to state changes
- Transition not cleaning up when leaving composition
- Multiple transition states conflicting

## Fixes

- Use rememberTransition for state-based animations
- Define clear state hierarchy
- Use transition.isRunning to detect active animations
- Clean up transitions on disposal

## Code Example

```kotlin
val expanded = remember { mutableStateOf(false) }
val transition = updateTransition(expanded, label = "expand")

val cardSize by transition.animateDp(label = "size") { isExpanded ->
    if (isExpanded) 300.dp else 150.dp
}

val cardColor by transition.animateColor(label = "color") { isExpanded ->
    if (isExpanded) MaterialTheme.colorScheme.primary
    else MaterialTheme.colorScheme.surface
}

val cornerRadius by transition.animateDp(label = "corner") { isExpanded ->
    if (isExpanded) 16.dp else 8.dp
}

Card(
    modifier = Modifier.size(cardSize),
    shape = RoundedCornerShape(cornerRadius),
    colors = CardDefaults.cardColors(containerColor = cardColor)
)
```

# updateTransition: state-driven animations
# animateDp, animateColor, animateFloat per property
# label: for animation debugging
# All properties animate together
