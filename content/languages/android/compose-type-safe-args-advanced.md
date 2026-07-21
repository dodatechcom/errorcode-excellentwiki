---
title: "Type Safe Args Advanced Error"
description: "Fix advanced type-safe navigation arguments with complex types in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Complex navigation argument types fail to serialize or deserialize

## Common Causes

- Enum type not properly serialized
- List arguments not supported in routes
- Parcelable objects not passed correctly
- Default values not working for complex types

## Fixes

- Use enum types with @Serializable
- Pass complex types via SavedStateHandle
- Use Parcelable for complex objects
- Provide defaults for all optional arguments

## Code Example

```kotlin
// Enum argument
@Serializable
enum class Category { FOOD, TRAVEL, TECH }

@Serializable
data class SearchRoute(
    val query: String,
    val category: Category = Category.FOOD
)

// Navigate:
navController.navigate(SearchRoute("kotlin", Category.TECH))

// In composable:
composable<SearchRoute> { backStackEntry ->
    val route = backStackEntry.toRoute<SearchRoute>()
    SearchScreen(route.query, route.category)
}
```

# Enum types: use @Serializable enum
# Complex types: use SavedStateHandle
# Parcelable: for complex objects
# Defaults: provide for optional args
