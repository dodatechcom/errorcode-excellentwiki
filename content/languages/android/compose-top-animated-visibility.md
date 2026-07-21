---
title: "AnimatedVisibility Error"
description: "Fix Compose AnimatedVisibility for enter/exit animation configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
AnimatedVisibility not animating correctly or not appearing/disappearing as expected

## Common Causes

- Content appearing without animation
- Animation not matching expected enter/exit
- Content not removed from composition after exit
- Animation interfering with other composables

## Fixes

- Configure enter and exit animations
- Use fadeIn/fadeOut, slideInVertically, expandVertically
- Ensure content is inside AnimatedVisibility block
- Test with different animation combinations

## Code Example

```kotlin
AnimatedVisibility(
    visible = isVisible,
    enter = fadeIn() + expandVertically(),
    exit = fadeOut() + shrinkVertically()
) {
    Text("Animated content")
}

// Cross-fade between content:
AnimatedContent(
    targetState = currentPage,
    transitionSpec = {
        fadeIn() + slideInHorizontally { it } with fadeOut()
    }
) { page ->
    PageContent(page)
}
```

# fadeIn/fadeOut: opacity animation# slideIn/slideOut: position animation# expandVertically/shrinkVertically: size animation# Cross-fade with AnimatedContent
