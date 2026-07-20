---
title: "[Solution] Kotlin Compose Navigation — NavHost, BackStackEntry, savedStateHandle"
description: "Fix Compose navigation errors. Learn correct NavHost setup, BackStackEntry handling, and savedStateHandle usage."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1023
---

## What This Error Means

Compose navigation errors occur when route definitions are incorrect, navigation arguments are not properly decoded, or savedStateHandle is used incorrectly. Common in apps using `navigation-compose`.

## Common Causes

- Route string mismatch between `composable("route")` and `navController.navigate("wrong")`
- Missing type-safe arguments in navigation
- Accessing `savedStateHandle` before navigation completes
- Wrong `NavHost` start destination

```kotlin
// Route mismatch
navController.navigate("user/123")
// But composable expects:
composable("user/{userId}") { backStackEntry ->
    val userId = backStackEntry.arguments?.getString("userId")
}
```

## How to Fix

**1. Define routes as constants or sealed classes**

```kotlin
sealed class Screen(val route: String) {
    object Home : Screen("home")
    object UserDetail : Screen("user/{userId}") {
        fun createRoute(userId: Long) = "user/$userId"
    }
}

// Navigate with type safety
navController.navigate(Screen.UserDetail.createRoute(123L))
```

**2. Extract arguments safely**

```kotlin
composable(
    "user/{userId}",
    arguments = listOf(navArgument("userId") { type = NavType.LongType })
) { backStackEntry ->
    val userId = backStackEntry.arguments?.getLong("userId") ?: return@composable
    UserScreen(userId)
}
```

**3. Use savedStateHandle for result passing**

```kotlin
// Previous screen
navController.currentBackStackEntry?.savedStateHandle?.set("result", "data")

// Receiving screen
val result = navController.previousBackStackEntry?.savedStateHandle?.get<String>("result")
```

**4. Use navigation-compose type-safe navigation (Compose 2.8+)**

```kotlin
@Serializable data class UserDetail(val userId: Long)

NavHost(navController, startDestination = Home) {
    composable<Home> { HomeScreen(navController) }
    composable<UserDetail> { backStackEntry ->
        val args = backStackEntry.toRoute<UserDetail>()
        UserDetailScreen(args.userId)
    }
}
```

## Examples

```kotlin
// Example 1: Complete NavHost setup
@Composable
fun AppNavigation() {
    val navController = rememberNavController()
    NavHost(navController, startDestination = "home") {
        composable("home") { HomeScreen(navController) }
        composable("settings") { SettingsScreen() }
        composable(
            "profile/{id}",
            arguments = listOf(navArgument("id") { type = NavType.IntType })
        ) { backStackEntry ->
            val id = backStackEntry.arguments?.getInt("id") ?: return@composable
            ProfileScreen(id)
        }
    }
}

// Example 2: Deep link support
composable(
    "product/{productId}",
    deepLinks = listOf(navDeepLink { uriPattern = "myapp://product/{productId}" })
) { backStackEntry ->
    val productId = backStackEntry.arguments?.getString("productId")
    ProductScreen(productId)
}

// Example 3: Nested navigation
navigation(startDestination = "nested_home", route = "nested") {
    composable("nested_home") { ... }
    composable("nested_detail/{id}") { ... }
}
```

## Related Errors

- [Compose recomposition](kotlin-compose-recomposition) — excessive recomposition
- [Compose side effect](kotlin-compose-side-effect) — effect lifecycle
- [Compose modifier error](kotlin-compose-modifier-error) — modifier issues
