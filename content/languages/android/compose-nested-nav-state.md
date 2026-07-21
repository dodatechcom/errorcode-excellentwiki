---
title: "Nested Navigation State Error"
description: "Fix nested navigation graph state management and preservation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
State in nested navigation destinations not properly preserved when switching tabs

## Common Causes

- State lost when switching between bottom nav tabs
- Nested back stack not properly managed
- ViewModel scoped to wrong graph
- State restoration not working after process death

## Fixes

- Use saveState/restoreState for bottom navigation
- Scope ViewModel to correct nav graph
- Use NavHost with separate back stack per tab
- Test state preservation across navigation

## Code Example

```kotlin
// Bottom navigation with state preservation
@Composable
fun AppNavHost(navController: NavHostController) {
    NavHost(navController, startDestination = "home") {
        navigation(startDestination = "home_tab", route = "home_graph") {
            composable("home_tab") {
                HomeScreen()
            }
            composable("detail/{id}") {
                DetailScreen()
            }
        }
        navigation(startDestination = "search_tab", route = "search_graph") {
            composable("search_tab") {
                SearchScreen()
            }
        }
    }
}

// With bottom nav:
navController.navigate(route) {
    popUpTo(navController.graph.findStartDestination().id) {
        saveState = true
    }
    launchSingleTop = true
    restoreState = true
}
```

# saveState: save state when leaving tab
# restoreState: restore state when returning
# launchSingleTop: prevent duplicate tabs
# popUpTo startDestination: clear back stack
