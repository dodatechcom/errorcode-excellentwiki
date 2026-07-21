---
title: "Crossfade Animation Error"
description: "Fix Crossfade animation errors when switching between Compose content"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Crossfade shows wrong content or does not animate between states

## Common Causes

- Crossfade target not properly keyed
- Animation duration too fast to see
- Content flickering during crossfade
- Crossfade used with complex composable trees

## Fixes

- Use correct targetState parameter
- Set appropriate animationSpec duration
- Use key parameter for stable animation
- Consider AnimatedContent for complex transitions

## Code Example

```kotlin
var currentScreen by remember { mutableStateOf("home") }

Crossfade(
    targetState = currentScreen,
    animationSpec = tween(durationMillis = 300),
    label = "screen_transition"
) { screen ->
    when (screen) {
        "home" -> HomeScreen()
        "profile" -> ProfileScreen()
        "settings" -> SettingsScreen()
    }
}
```

# Crossfade: simple content swap
# AnimatedContent: complex state transitions
# Use key/targetState for stable animations
