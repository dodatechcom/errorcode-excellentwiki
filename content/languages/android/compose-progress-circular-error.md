---
title: "Circular Progress Determinate Error"
description: "Fix Material 3 CircularProgressIndicator determinate mode errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
CircularProgressIndicator does not display correct progress value

## Common Causes

- Progress value not updating visually
- Progress color not matching design
- Progress indicator size too small
- Indeterminate vs determinate mode wrong

## Fixes

- Set progress parameter for determinate mode
- Use color and trackColor for custom colors
- Set strokeWidth and modifier.size for dimensions
- Leave progress null for indeterminate

## Code Example

```kotlin
// Determinate progress
CircularProgressIndicator(
    progress = { 0.75f },
    modifier = Modifier.size(48.dp),
    color = MaterialTheme.colorScheme.primary,
    trackColor = MaterialTheme.colorScheme.surfaceVariant,
    strokeWidth = 4.dp
)

// Animated progress
val progress by animateFloatAsState(
    targetValue = downloadProgress,
    animationSpec = tween(300)
)
CircularProgressIndicator(
    progress = { progress },
    modifier = Modifier.size(64.dp)
)
```

# progress: null for indeterminate, 0f-1f for determinate
# color: progress indicator color
# trackColor: background track color
# strokeWidth: thickness of indicator
