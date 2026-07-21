---
title: "Nested Navigation Graph Error"
description: "Fix nested navigation graph errors in Jetpack Compose Navigation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Nested navigation graphs do not navigate correctly between destinations

## Common Causes

- Nested navDestination not reachable from parent
- Navigation action ID not matching nested destination
- Back stack not properly managed with nested graphs
- Arguments not passed to nested destinations

## Fixes

- Define nested navigation as navGraph inside parent
- Use explicit action IDs for nested navigation
- Manage back stack per nested graph
- Pass arguments with proper path or query parameters

## Code Example

```kotlin
navGraph("home") {
    startDestination("list")

    composable("list") {
        ListScreen(onItemClick = { id ->
            navController.navigate("detail/$id")
        })
    }

    composable(
        "detail/{itemId}",
        arguments = listOf(navArgument("itemId") { type = NavType.IntType })
    ) { backStackEntry ->
        val itemId = backStackEntry.arguments?.getInt("itemId")
        DetailScreen(itemId = itemId)
    }
}
```

# Nested graphs have their own back stack
# Use navGraph {} for nested navigation
# Arguments passed via route template
