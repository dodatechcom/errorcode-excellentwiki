---
title: "AnimatedContent Error"
description: "Fix AnimatedContent transition and state management errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
AnimatedContent does not transition between states correctly

## Common Causes

- targetState not properly defined
- Transition animations conflicting
- Content not matching current state
- Label not provided for debugging

## Fixes

- Define targetState for content switching
- Use proper enter/exit transitions
- Match content to current targetState
- Provide label for animation debugging

## Code Example

```kotlin
var currentState by remember { mutableStateOf("home") }

AnimatedContent(
    targetState = currentState,
    transitionSpec = {
        if (targetState == "detail") {
            slideInHorizontally { it } + fadeIn() togetherWith
            slideOutHorizontally { -it } + fadeOut()
        } else {
            slideInHorizontally { -it } + fadeIn() togetherWith
            slideOutHorizontally { it } + fadeOut()
        }
    },
    label = "screen_transition"
) { state ->
    when (state) {
        "home" -> HomeScreen()
        "detail" -> DetailScreen()
    }
}
```

# targetState: drives the content switch
# transitionSpec: defines enter/exit animations
# togetherWith: combine enter and exit
# label: for animation debugging
