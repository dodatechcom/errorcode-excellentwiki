---
title: "Offset Modifier Error"
description: "Fix Compose offset modifier for positioning composable without affecting layout"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable offset not positioning correctly or affecting parent layout

## Common Causes

- Offset not moving composable as expected
- Offset affecting parent layout instead of just visual
- Offset values not matching expected positions
- Offset causing composables to overlap

## Fixes

- Use offset modifier for visual-only positioning
- Use absoluteOffset for pixel-based offset
- Ensure offset does not affect layout
- Test offset with different parent layouts

## Code Example

```kotlin
Modifier.offset(x = 16.dp, y = 8.dp)

// Absolute offset (pixels):
Modifier.absoluteOffset(x = 100f, y = 50f)

// IntOffset:
Modifier.offset { IntOffset(100, 50) }
```

# offset: visual-only positioning# absoluteOffset: pixel-based# offset { IntOffset }: dynamic offset# Does not affect parent layout
