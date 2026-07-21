---
title: "Press Indication Error"
description: "Fix Compose press indication and ripple effect errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Ripple or press indication does not show when composable is pressed

## Common Causes

- indication modifier not applied
- RippleTheme not providing correct colors
- Press state not tracked
- Material components not showing ripple automatically

## Fixes

- Add indication modifier with ripple()
- Configure RippleTheme for custom ripple
- Use interactionSource to track press state
- Material buttons show ripple automatically

## Code Example

```kotlin
// Basic ripple
Box(
    modifier = Modifier
        .clickable(
            interactionSource = interactionSource,
            indication = rememberRipple()
        ) { onClick() }
)

// Custom ripple theme
@Composable
fun CustomRippleTheme() = RippleTheme(
    color = MaterialTheme.colorScheme.primary,
    lightTheme = MaterialTheme.colorScheme.surface,
    darkTheme = MaterialTheme.colorScheme.onSurface
)

// Track press state:
val interactionSource = remember { MutableInteractionSource() }
val isPressed by interactionSource.collectIsPressedAsState()

Box(
    modifier = Modifier
        .background(if (isPressed) Color.LightGray else Color.White)
        .clickable(
            interactionSource = interactionSource,
            indication = rememberRipple()
        ) { onClick() }
)
```

# clickable provides ripple automatically
# indication: visual feedback for press
# interactionSource: track press/hover/drag states
