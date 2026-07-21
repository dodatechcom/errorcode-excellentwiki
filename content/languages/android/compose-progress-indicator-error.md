---
title: "Progress Indicator Error"
description: "Fix Material 3 LinearProgressIndicator and CircularProgressIndicator errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Progress indicators do not display correctly or animate smoothly

## Common Causes

- Indicator not showing progress value
- Indeterminate animation not playing
- Indicator color not matching theme
- Indicator size not appropriate for context

## Fixes

- Set progress parameter for determinate indicator
- Leave progress null for indeterminate
- Use indicatorColor and trackColor parameters
- Size indicator appropriately for context

## Code Example

```kotlin
// Determinate progress
var progress by remember { mutableStateOf(0.5f) }
LinearProgressIndicator(
    progress = { progress },
    modifier = Modifier.fillMaxWidth(),
    color = MaterialTheme.colorScheme.primary,
    trackColor = MaterialTheme.colorScheme.surfaceVariant
)

// Indeterminate (no progress value)
CircularProgressIndicator(
    modifier = Modifier.size(48.dp),
    color = MaterialTheme.colorScheme.primary,
    strokeWidth = 4.dp
)
```

# LinearProgressIndicator: horizontal bar
# CircularProgressIndicator: circular spinner
# progress: null for indeterminate, 0f-1f for determinate
# color/trackColor: customize appearance
