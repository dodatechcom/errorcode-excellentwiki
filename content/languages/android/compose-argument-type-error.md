---
title: "Navigation Argument Type Error"
description: "Fix Navigation argument type errors in Compose destinations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Navigation arguments are wrong type or not properly parsed

## Common Causes

- Argument declared as Int but passed as String
- Nullable arguments not handled
- Complex object not serializable for navigation
- Default value not matching expected type

## Fixes

- Match argument types between declaration and usage
- Handle nullable arguments with required=false
- Use Parcelable or Serializable for complex objects
- Provide matching default values

## Code Example

```kotlin
// Declaration with types:
composable(
    route = "detail/{itemId}?name={name}",
    arguments = listOf(
        navArgument("itemId") { type = NavType.IntType },
        navArgument("name") {
            type = NavType.StringType
            nullable = true
            defaultValue = null
        }
    )
) { backStackEntry ->
    val itemId = backStackEntry.arguments?.getInt("itemId")
    val name = backStackEntry.arguments?.getString("name")
}

// Navigation with arguments:
navController.navigate("detail/123?name=John")
```

# NavType.IntType, NavType.StringType, etc.
# nullable = true for optional arguments
# Default values must match declared type
