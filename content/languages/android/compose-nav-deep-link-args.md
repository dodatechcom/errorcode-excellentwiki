---
title: "Deep Link Argument Error"
description: "Fix deep link argument parsing and type conversion errors in Compose Navigation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Deep link arguments are not properly parsed or converted to correct types

## Common Causes

- Argument in URI not matching declared navArgument
- Type conversion failing for deep link arguments
- Query parameter not extracted correctly
- Path parameter not available in composable

## Fixes

- Match URI pattern exactly with argument declarations
- Use correct NavType for each argument
- Extract query parameters from URI
- Use backStackEntry.arguments to read values

## Code Example

```kotlin
composable(
    route = "product/{productId}",
    deepLinks = listOf(
        navDeepLink { uriPattern = "myapp://product/{productId}" }
    ),
    arguments = listOf(
        navArgument("productId") { type = NavType.IntType }
    )
) { backStackEntry ->
    val productId = backStackEntry.arguments?.getInt("productId")
    ProductScreen(productId = productId ?: 0)
}

// Query parameters:
navDeepLink { uriPattern = "myapp://search?q={query}" }
// Extract: backStackEntry.arguments?.getString("query")
```

# URI pattern must match navArgument declarations
# Use correct NavType: IntType, StringType, etc.
# Path params: {paramName} in URI
# Query params: ?key=value in URI
