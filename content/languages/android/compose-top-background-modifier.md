---
title: "Background Modifier Error"
description: "Fix Compose background modifier for custom background drawing and theming"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Background modifier not drawing correctly or not matching expected appearance

## Common Causes

- Background not covering full composable area
- Background shape not matching expected outline
- Background color not changing with theme
- Background overlapping content incorrectly

## Fixes

- Use background modifier with color or brush
- Use background with shape for rounded corners
- Test with different background configurations
- Ensure background does not overlap content

## Code Example

```kotlin
Modifier
    .background(Color.Red)
    .padding(16.dp)

// With shape:
Modifier
    .background(
        color = MaterialTheme.colorScheme.surface,
        shape = RoundedCornerShape(8.dp)
    )
    .padding(16.dp)

// With brush:
Modifier
    .background(
        brush = Brush.verticalGradient(
            colors = listOf(Color.Red, Color.Blue)
        )
    )
    .padding(16.dp)
```

# background(color): solid color background# background(brush): gradient background# background(shape): shaped background# Order matters: background then padding
