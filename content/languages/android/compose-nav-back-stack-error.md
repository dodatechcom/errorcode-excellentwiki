---
title: "Navigation Back Stack Error"
description: "Fix Compose navigation back stack management and pop behavior errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Back button does not behave as expected or back stack is corrupted

## Common Causes

- popUpTo removing wrong destinations
- Back stack entry duplicated on repeated navigation
- Back button not returning to previous screen
- Bottom nav destinations not preserving back stack

## Fixes

- Configure popUpTo correctly in navOptions
- Use launchSingleTop to prevent duplicates
- Use restoreState for bottom navigation
- Manage back stack per navigation graph

## Code Example

```kotlin
// Bottom navigation with back stack preservation
navController.navDestination("home") {
    composable("home") {
        HomeScreen()
    }
    composable("search") {
        SearchScreen()
    }
    composable("profile") {
        ProfileScreen()
    }
}

// Navigation with proper back stack:
navController.navigate("detail/$id") {
    popUpTo(navController.graph.findStartDestination().id) {
        saveState = true
    }
    launchSingleTop = true
    restoreState = true
}
```

# saveState: save state of popped destinations
# restoreState: restore state when returning
# launchSingleTop: prevent duplicate entries
# popUpTo startDestination for bottom nav
