---
title: "AnimatedVisibility Error"
description: "Fix AnimatedVisibility enter/exit transition errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
AnimatedVisibility does not animate or produces visual glitches

## Common Causes

- EnterTransition and ExitTransition not properly configured
- Content not appearing after animation completes
- Animation playing on initial composition
- Multiple animations conflicting

## Fixes

- Configure enter and exit transitions explicitly
- Use remember to control visibility state
- Set initiallyVisible parameter if needed
- Use animateEnterAsState for complex animations

## Code Example

```kotlin
var visible by remember { mutableStateOf(true) }

AnimatedVisibility(
    visible = visible,
    enter = fadeIn() + slideInVertically(),
    exit = fadeOut() + slideOutVertically()
) {
    Text("Animated Content")
}

// Full screen transition:
AnimatedVisibility(
    visible = isVisible,
    enter = expandVertically() + fadeIn(),
    exit = shrinkVertically() + fadeOut()
) {
    ExpandedContent()
}
```

# Enter: fadeIn, slideIn, expandIn, etc.
# Exit: fadeOut, slideOut, shrinkOut, etc.
# Combine transitions with + operator
