---
title: "Compose Navigation Error"
description: "Fix Jetpack Compose navigation errors with NavHost and route configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Navigation between Compose screens fails with route or argument errors

## Common Causes

- Route string does not match defined navDestination
- Missing required navigation argument
- NavHost not properly configured with NavController
- Deep link route format incorrect

## Fixes

- Define routes as constants matching navController.navigate calls
- Use navArgument to define required arguments
- Set up NavHost with correct startDestination
- Format deep links with proper URI pattern

## Code Example

```kotlin
NavHost(navController = navController, startDestination = "home") {
    composable("home") {
        HomeScreen(onNavigate = { navController.navigate("detail/$id") })
    }
    composable(
        route = "detail/{itemId}",
        arguments = listOf(navArgument("itemId") { type = NavType.IntType })
    ) { backStackEntry ->
        val itemId = backStackEntry.arguments?.getInt("itemId")
        DetailScreen(itemId = itemId)
    }
}
```

# Use type-safe navigation (Compose Navigation 2.8+)
# Or define routes as const val strings
