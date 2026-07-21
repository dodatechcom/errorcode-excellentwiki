---
title: "Alpha Modifier Error"
description: "Fix Compose alpha modifier for transparency and opacity control"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable transparency not applying correctly or causing rendering issues

## Common Causes

- Alpha not making composable transparent
- Alpha value not matching expected opacity
- Alpha causing text rendering issues
- Alpha not working with background

## Fixes

- Use alpha modifier with float value
- Test alpha with different content types
- Ensure alpha does not affect text readability
- Use alpha for visual-only transparency

## Code Example

```kotlin
Modifier.alpha(0.5f)  // 50% transparent

// Conditional alpha:
Modifier.alpha(if (isEnabled) 1f else 0.5f)

// Animated alpha:
val alpha by animateFloatAsState(
    targetValue = if (isVisible) 1f else 0f,
    animationSpec = tween(durationMillis = 300)
)
Modifier.alpha(alpha)
```

# alpha(float): transparency 0-1# Conditional alpha for enabled/disabled# Animated alpha for transitions# Test with different content types
