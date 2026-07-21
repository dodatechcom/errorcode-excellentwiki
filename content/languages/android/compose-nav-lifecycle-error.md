---
title: "Navigation Lifecycle Error"
description: "Fix Compose navigation lifecycle and state restoration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose navigation destinations lose state when navigating away and back

## Common Causes

- Destination state not saved when navigating away
- Back stack entry cleared on deep navigation
- ViewModel state not persisting across navigation
- Fragment result not being delivered between destinations

## Fixes

- Use rememberSaveable for navigation destination state
- Use ViewModel for persistent state
- Configure navOptions to keep back stack
- Use fragment result API for inter-destination communication

## Code Example

```kotlin
// Navigation with state preservation
navController.navigate("detail/$id") {
    launchSingleTop = true
    restoreState = true
    popUpTo("home") {
        saveState = true
    }
}

// Save state in destination:
@Composable
fun DetailScreen(itemId: Int) {
    var scrollPosition by rememberSaveable { mutableStateOf(0) }
    // scrollPosition survives navigation
}
```

# restoreState: restore state when returning
# saveState: save state when leaving
# launchSingleTop: prevent duplicate destinations
# ViewModel: survives navigation changes
