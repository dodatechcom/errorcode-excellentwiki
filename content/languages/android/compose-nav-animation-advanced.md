---
title: "Navigation Animation Advanced Error"
description: "Fix advanced navigation transition animations with shared elements in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Shared element transitions between navigation destinations not working

## Common Causes

- Shared element not animating between screens
- Transition not matching expected start/end states
- Animation spec not configured correctly
- Shared element key not unique

## Fixes

- Use SharedTransitionLayout for shared elements
- Configure enterTransition and exitTransition
- Use sharedElement modifier with sharedTransitionScope
- Ensure shared element keys are unique

## Code Example

```kotlin
// Shared element transition
composable(
    route = "detail/{id}",
    enterTransition = { fadeIn() + slideInHorizontally() },
    exitTransition = { fadeOut() + slideOutHorizontally() }
) {
    DetailScreen()
}

// With shared element:
SharedTransitionLayout {
    NavHost(navController, startDestination = "home") {
        composable("home") { entry ->
            ListItem(
                modifier = Modifier.sharedElement(
                    sharedTransitionScope = this@SharedTransitionLayout,
                    sharedContentKey = "item_123"
                )
            )
        }
        composable("detail") { entry ->
            DetailScreen(
                modifier = Modifier.sharedElement(
                    sharedTransitionScope = this@SharedTransitionLayout,
                    sharedContentKey = "item_123"
                )
            )
        }
    }
}
```

# SharedTransitionLayout: shared element container
# sharedElement: element to animate
# sharedContentKey: unique key for matching
# enterTransition/exitTransition: screen transitions
